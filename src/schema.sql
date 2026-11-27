CREATE TABLE refs (
    id INTEGER PRIMARY KEY,
    citekey TEXT UNIQUE,
    type TEXT NOT NULL
   );

CREATE TABLE books (
    viite_id INTEGER PRIMARY KEY REFERENCES refs(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL,
    editor TEXT, -- all books do not have editor so this as mandatory is kinda redundant?
    publisher TEXT NOT NULL,
    volume INTEGER,
    number INTEGER,
    pages TEXT,
    month TEXT,
    note TEXT,
    doi TEXT,
    issn TEXT,
    isbn TEXT
);

CREATE TABLE inproceedings (
    -- on delete cascade poistaa automaattisesti viitatut child row't
    viite_id INTEGER PRIMARY KEY REFERENCES refs(id) ON DELETE CASCADE,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    booktitle TEXT NOT NULL,
    year TEXT NOT NULL,
    editor TEXT,
    volume TEXT,
    series TEXT,
    address TEXT,
    organization TEXT,
    publisher TEXT,
    pages TEXT,
    month TEXT,
    doi TEXT,
    url TEXT,
    isbn,
    note TEXT
);

CREATE TABLE articles (
    viite_id INTEGER PRIMARY KEY REFERENCES refs(id) ON DELETE CASCADE,
    author TEXT NOT NULL,
    title TEXT NOT NULL,
    journal TEXT NOT NULL,
    year TEXT NOT NULL,
    volume TEXT,
    number TEXT,
    pages TEXT,
    month TEXT,
    doi TEXT,
    issn TEXT,
    zblnumber TEXT,
    eprint TEXT,
    note TEXT
);
