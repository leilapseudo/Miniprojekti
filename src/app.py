from flask import render_template, request, jsonify
from entities.reference import Book
from db_helper import reset_db
from config import app, test_env

refs = []

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        ref = ""
        for item in request.form.items():
            ref = ref + item[0] + ": " + item[1] + ",  "
        refs.append(ref)
    book = Book()
    print(book.fields["required"])
    return render_template("index.html", reference = book, refs = refs)





# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
