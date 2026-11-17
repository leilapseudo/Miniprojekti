from flask import redirect, render_template, request, jsonify, flash
from entities.reference import Reference, Book
from db_helper import reset_db
from config import app, test_env

@app.route("/")
def index():
    book = Book()
    print(book.fields["required"])
    return render_template("index.html", reference = book) 

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
