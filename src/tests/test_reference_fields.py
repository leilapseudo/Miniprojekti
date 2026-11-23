from entities.reference import Reference, Book


def test_reference_stores_given_fields():
    ref = Reference(["author"], ["note"], ["doi"], "misc")

    assert ref.type == "misc"
    assert ref.required == ["author"]
    assert ref.optional == ["note"]
    assert ref.non_standard == ["doi"]


def test_reference_fields_dict_groups_fields():
    ref = Reference(["a"], ["b"], ["c"], "misc")

    assert ref.fields == {
        "required": ["a"],
        "optional": ["b"],
        "non_standard": ["c"],
    }


def test_book_optional_fields():
    book = Book()
    
    for field in ["volume", "number", "pages", "month", "note"]:
        assert field in book.fields["optional"]


def test_book_non_standard_fields():
    book = Book()

    for field in ["doi", "issn", "isbn"]:
        assert field in book.fields["non_standard"]