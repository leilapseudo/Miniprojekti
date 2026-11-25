from entities.reference import Book


def test_book_type():
    assert Book().type == "book"


def test_book_has_required_fields():
    book = Book()
    for field in ["author", "title", "publisher", "year"]:
        assert field in book.fields["required"]
