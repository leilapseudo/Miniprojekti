from sqlalchemy import text
from db_helper import tables
from config import db
from entities.reference import ReferenceBuilder
from .utils import validate_fields



def get_books():
    book_res = db.session.execute(text("SELECT * FROM refs INNER JOIN books ON refs.id = books.viite_id"))
    book_refs = book_res.fetchall()
    inproceedings_res = db.session.execute(text("SELECT * FROM refs INNER JOIN inproceedings ON refs.id = inproceedings.viite_id")).fetchall()
    articles_res = db.session.execute(text("SELECT * FROM refs INNER JOIN articles ON refs.id = articles.viite_id")).fetchall()
    ref_objects = []
    for res in book_refs:
        ref_objects.append(row_to_ref(res))
    for res in inproceedings_res:
        ref_objects.append(row_to_ref(res))
    for res in articles_res:
        ref_objects.append(row_to_ref(res))

    return ref_objects

def get_book(book_id):
    res = db.session.execute(
        text("SELECT type FROM refs WHERE id = :id"),
        {"id": book_id}
    )
    ref_type = res.fetchone()
    if ref_type:
        table = ReferenceBuilder().build_reference(ref_type=ref_type[0]).db_table
    else:
        table = None
    res = db.session.execute(text(f"SELECT * FROM {table} WHERE {table}.viite_id = :id"), {"id": book_id})
    return row_to_ref(res.fetchone(), ref_type[0])


def get_inproceedings():
    pass

def get_articles():
    pass

def get_references():
    list_of_all_refs = []
    list_of_all_refs.append(get_books())
    return list_of_all_refs

def add_reference(reference):
    reference = request_to_ref(reference)
    query = text("INSERT INTO refs (type) VALUES (:type) ")
    query_res = db.session.execute(query, {"type": reference.type})
    last_id = query_res.lastrowid
    values = reference.info
    validate_fields(reference.get_all_fields(), reference.info)
    values["viite_id"] = last_id
    columns = list(values)
    table = reference.db_table
    column_names = ", ".join(columns)
    value_parameters = ", ".join(f":{column}" for column in columns)
    query = text(f"INSERT INTO {table} ({column_names}) VALUES ({value_parameters})")
    db.session.execute(query, values)
    db.session.commit()

def update_book(book_id, reference):
    print("TYPE", reference)
    reference = (ReferenceBuilder().build_reference(f"{reference.pop("type")}", ref_object=reference))
    reference.info["viite_id"] = book_id
    columns = list(reference.info.keys())

    if reference.db_table not in tables():
        raise ValueError("ILLEGITIMATE FIELDS")
    assignments = ", ".join(f"{column} = :{column}" for column in columns)
    query = text(f"UPDATE {reference.db_table} SET {assignments} WHERE viite_id = :viite_id")
    db.session.execute(query, reference.info)
    db.session.commit()

def delete_book(book_id):
    db.session.execute(text("DELETE FROM books WHERE viite_id = :viite_id"), {"viite_id": book_id})
    db.session.execute(text("DELETE FROM inproceedings WHERE viite_id = :viite_id"), {"viite_id": book_id})
    db.session.execute(text("DELETE FROM articles WHERE viite_id = :viite_id"), {"viite_id": book_id})
    db.session.execute(text("DELETE FROM refs WHERE id = :viite_id"), {"viite_id": book_id})
    db.session.commit()

def request_to_ref(request_form_object):
    req_as_dict = request_form_object.to_dict()
    print(req_as_dict)
    ref_type = req_as_dict.pop("type")
    return ReferenceBuilder().build_reference(f"{ref_type}", ref_object=req_as_dict)

def row_to_ref(row_object, def_type=None):
    if row_object:
        initializer_dict = {}
        for k, v in zip(row_object._fields, row_object):
            initializer_dict[k] = v
        ref_id = initializer_dict.pop("viite_id")
        return ReferenceBuilder().build_reference(initializer_dict.pop("type", def_type), ref_object=initializer_dict, ref_id=ref_id)
    return ValueError("NO ROW")
