from entities.reference import Reference, Book


def test_reference_stores_fields():
    ref = Reference(["title"], ["note"], ["doi"], "misc")
    assert ref.type == "misc"
    assert ref.fields == {
        "required": ["title"],
        "optional": ["note"],
        "non_standard": ["doi"],
    }


def test_book_type_is_book():
    assert Book().type == "book"


def test_book_has_title_and_publisher_as_required():
    book = Book()
    assert "title" in book.fields["required"]
    assert "publisher" in book.fields["required"]


def test_book_non_standard_fields():
    assert Book().fields["non_standard"] == ["doi", "issn", "isbn"]
