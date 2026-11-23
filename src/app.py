from flask import render_template, request, jsonify
from entities.reference import Book
from db_helper import reset_db
from config import app, test_env
from repositories import reference_repository

refs = []

@app.route("/", methods=['GET', "POST"])
def index():
    book_refs = reference_repository.get_books()
    print(book_refs)
    book = Book()
    print(book.fields["required"])
    return render_template("index.html", reference = book, refs = refs)

@app.route("/references", methods=["POST"])
def new_reference():
        ref = ""
        for item in request.form.items():
            ref = ref + item[0] + ": " + item[1] + ",  "
<<<<<<< HEAD
        refs.append(ref)     
        return redirect("/")
=======
        refs.append(ref)
    book = Book()
    print(book.fields["required"])
    return render_template("index.html", reference = book, refs = refs)

>>>>>>> e7576bd9bd039b2e98e62ee625f0e9cc48b8ee8f




# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
