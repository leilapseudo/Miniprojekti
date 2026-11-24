from sqlalchemy import text
from config import db
from entities.reference import Book

def get_books():
    res = db.session.execute(text("SELECT * FROM books"))
    book_refs = res.fetchall()
    return book_refs

def get_book(book_id):
    res = db.session.execute(
        text("SELECT * FROM books WHERE viite_id = :id"),
        {"id": book_id}
    )
    return res.fetchone()

def get_inproceedings():
    pass

def get_references():
    list_of_all_refs = []
    list_of_all_refs.append(get_books())
    return list_of_all_refs

def add_reference(reference):
    ref_type = "book"
    #Implement support for inproceeding, article etc by matching with type of ref requested later
    #Could add a timestamp created_at in the future, that would be common across all references
    query = text("INSERT INTO refs (type) VALUES (:type) ")
    query_res = db.session.execute(query, {"type": ref_type})
    last_id = query_res.lastrowid
    if ref_type == "book":
        add_book(reference, last_id)
    db.session.commit()

def add_book(reference, book_id):
    #This long check is needed to protect against SQL injection
    #because sql doesn't let us populate columns dynamically
    allowed_fields = []
    for field in Book().fields["required"]:
        allowed_fields.append(field)
    for field in Book().fields["optional"]:
        allowed_fields.append(field)
    for field in Book().fields["non_standard"]:
        allowed_fields.append(field)
    if not all(field in allowed_fields for field in reference.keys()):
        print("Invalid fields")

    values = dict(reference.items())
    values["viite_id"] = book_id
    columns = list(values)
    column_names = ", ".join(columns)
    value_parameters = ", ".join(f":{column}" for column in columns)
    query = text(f"INSERT INTO books ({column_names}) VALUES ({value_parameters})")
    db.session.execute(query, values)

def update_book(book_id, reference):
    book = Book()
    allowed = book.fields["required"] + book.fields["optional"] + book.fields["non_standard"]
    if not all(field in allowed for field in reference.keys()):
        raise ValueError("Invalid fields")

    values = dict(reference.items())
    values["viite_id"] = book_id
    columns = list(reference.keys())
    assignments = ", ".join(f"{column} = :{column}" for column in columns)
    query = text(f"UPDATE books SET {assignments} WHERE viite_id = :viite_id")
    db.session.execute(query, values)
    db.session.commit()
