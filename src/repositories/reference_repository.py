from config import db
from sqlalchemy import text

def get_books():
    res = db.session.execute(text("SELECT * FROM books"))
    book_refs = res.fetchall()
    return book_refs

def get_inproceedings():
    pass

def get_references():
    list_of_all_refs = []
    list_of_all_refs.append(get_books())    
    return list_of_all_refs

def add_reference(reference):
    type = "book"
    #Implement support for inproceeding, article etc by matching with type of ref requested later   
    query = (text("INSERT INTO refs (type) VALUES (:type) "))
    query_res = db.session.execute(query, {"type": type})
    last_id = query_res.lastrowid
    add_book(reference, last_id)    

def add_book(reference):
    pass