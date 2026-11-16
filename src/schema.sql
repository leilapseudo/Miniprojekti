CREATE TABLE refs (
    id INTEGER PRIMARY KEY,
    citekey TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL,
    title TEXT NOT NULL,
    author TEXT,            -- nullable: on kirjoja, joissa vain editori
    year INTEGER NOT NULL
);

CREATE TABLE books (
    viite_id INTEGER PRIMARY KEY REFERENCES refs(id) ON DELETE CASCADE,
    editor TEXT, -- all books do not have editor so this as mandatory is kinda redundant?
    publisher TEXT NOT NULL,
    year_2 INT -- miksi references formissa year kaksi kertaa?
);
