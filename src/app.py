from flask import render_template, request, jsonify, redirect
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
    return render_template("index.html", reference = book, refs = book_refs)

@app.route("/references", methods=["POST"])
def new_reference():
    reference_repository.add_reference(request.form)
    ref = ""
    for item in request.form.items():
        ref = ref + item[0] + ": " + item[1] + ",  "

    refs.append(ref)
    return redirect("/")

@app.route("/references/<int:id>", methods=["GET", "PUT"])
def update_reference():
    pass

@app.route("/references/<int:id>", methods=["DELETE"])
def delete_reference():
    pass



# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
