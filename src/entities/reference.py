#Each field is a list of strings corresponding to the possible fields of a bibtex entry
class Reference:
    def __init__(self, required, optional, non_standard):
        self.required = required
        self.optional = optional
        self.non_standard = non_standard
        self.fields = {"required": self.required,
        "optional": self.optional, "non_standard": self.non_standard}

#Instance of a reference class for bibtex entry type "book"
class Book(Reference):
    def __init__(self):
        required = ['author', 'editor', 'title', 'publisher', 'year']
        optional = ['year', 'volume', 'number', 'pages', 'month', 'note']
        non_standard = ['doi', 'issn', 'isbn']
        super().__init__(required, optional, non_standard)