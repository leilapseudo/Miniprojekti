from entities.reference import Reference, Book, ReferenceBuilder


def test_builder_builds_correct():
    book = ReferenceBuilder().build_reference("book")
    inproceedings = ReferenceBuilder().build_reference("inproceedings")
    article = ReferenceBuilder().build_reference("article")
    types = (book.type, inproceedings.type, article.type)
    assert types == ("book", "inproceedings", "article")



def test_reference_fields_dict_groups_fields():
    ref = Reference(["a"], ["b"], ["c"], "misc", "book")

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
