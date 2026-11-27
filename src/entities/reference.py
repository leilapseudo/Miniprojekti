#Each field is a list of strings corresponding to the possible fields of a bibtex entry
class Reference:
    def __init__(self, required, optional, non_standard, db_table, ref_type, ref_id=None, ref_object=None):
        self.id = ref_id
        self.required = required
        self.optional = optional
        self.non_standard = non_standard
        self.type = ref_type
        self.fields = {"required": self.required,
        "optional": self.optional, "non_standard": self.non_standard}
        self.info = ref_object
        self.db_table = db_table

        if ref_object:
            for field, value in ref_object.items():
                self.info[field] = value

    def is_required(self, name_of_field):
        return name_of_field in self.fields["required"]

    def set_fields(self, dict_with_fields_and_values):
        for k, v in dict_with_fields_and_values:
            self.info[k] = v

    def set_id(self, ref_id):
        self.id = ref_id

    def get_all_fields(self):
        return self.fields["required"] + self.fields["optional"] + self.fields["non_standard"]

#Instance of a reference class for bibtex entry type "book"
class Book(Reference):
    def __init__(self, ref_object=None, ref_id=None):
        required = ['author', 'editor', 'title', 'publisher', 'year']
        optional = ['volume', 'number', 'pages', 'month', 'note']
        non_standard = ['doi', 'issn', 'isbn']
        super().__init__(required, optional, non_standard, "books", "book", ref_object=ref_object, ref_id = ref_id)

class Article(Reference):
    def __init__(self, ref_object=None, ref_id=None):
        required = ["author", "title", "journal", "year"]
        optional = ["volume", "number", "pages", "month", "note"]
        non_standard = ["doi", "issn", "zblnumber", "eprint"]
        super().__init__(required, optional, non_standard, "articles", "article", ref_object=ref_object, ref_id = ref_id)

class Inproceedings(Reference):
    def __init__(self, ref_object=None, ref_id=None):
        required = ["author", "title", "booktitle", "year"]
        optional = ["editor", "volume", "series", "address", "organization", "publisher", "pages", "month", "note"]
        non_standard = ["doi", "url", "isbn"]
        super().__init__(required, optional, non_standard, "inproceedings", "inproceedings", ref_object=ref_object, ref_id = ref_id)

class ReferenceBuilder():
    def __init__(self):
        self.ref_types = ["book", "inproceedings", "article"]

    def build_reference(self, ref_type, ref_id=None, ref_object=None):
        if ref_type == "book":
            return Book(ref_object=ref_object, ref_id=ref_id)
        if ref_type == "inproceedings":
            return Inproceedings(ref_object=ref_object, ref_id=ref_id)
        if ref_type == "article":
            return Article(ref_object=ref_object, ref_id=ref_id)

        return ValueError("NO SUCH REFERENCE TYPE IS IMPLEMENTED")

    def get_types(self):
        return self.ref_types
