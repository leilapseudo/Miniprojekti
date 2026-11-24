from flask import render_template, request, jsonify, redirect, abort
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

@app.route("/references/<int:book_id>", methods=["GET", "POST"])
def update_reference(book_id):
    if request.method == "GET":
        book = reference_repository.get_book(book_id)
        if book is None:
            abort(404)
        return render_template("edit_reference.html", reference=Book(), book=book)

    data = request.form.to_dict()
    reference_repository.update_book(book_id, data)
    return redirect("/")

@app.route("/edit")
def edit_redirect():
    book_id = request.args.get("id")
    if book_id is None:
        return redirect("/")
    return redirect(f"/references/{book_id}")

@app.route("/references/<int:id>", methods=["DELETE"])
def delete_reference():
    pass



# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
