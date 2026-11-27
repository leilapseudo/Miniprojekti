import re
from flask import render_template, request, jsonify, redirect, abort
from entities.reference import ReferenceBuilder
from db_helper import reset_db
from config import app, test_env
from repositories import reference_repository


@app.route("/", methods=['GET', "POST"])
def index():
    url_pattern_to_match = "book|article|inproceedings"
    match = re.search(url_pattern_to_match, request.url)
    form_type = "book"
    if match:
        form_type = match.group()
    book_refs = reference_repository.get_books()
    book = ReferenceBuilder().build_reference(form_type)
    return render_template("index.html", reference = book, refs = book_refs)

@app.route("/references", methods=["POST"])
def new_reference():
    reference_repository.add_reference(request.form)
    return redirect("/")

@app.route("/references/<int:book_id>", methods=["GET", "POST"])
def update_reference(book_id):
    if request.method == "GET":
        print(request.args.to_dict())
        reference = reference_repository.get_book(book_id)
        print("RE", reference)
        if reference is None:
            abort(404)
        return render_template("edit_reference.html", reference=reference, id=book_id)

    data = request.form.to_dict()
    reference_repository.update_book(book_id, data)
    return redirect("/")

@app.route("/edit")
def edit_redirect():
    book_id = request.args.get("id")
    if book_id is None:
        return redirect("/")
    return redirect(f"/references/{book_id}")

@app.route("/delete", methods=["POST"])
def delete_reference():
    book_id = request.form.get("id", type=int)
    if book_id is None:
        return redirect("/")
    reference_repository.delete_book(book_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })

if test_env:
    @app.route("/visualize_db")
    def visualize_db():
        pass
