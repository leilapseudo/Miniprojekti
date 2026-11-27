import os
from sqlalchemy import text
from config import db, app


def reset_db():
    setup_db()


def tables():
    """Returns all table names from the database"""
    sql = text(
        "SELECT name FROM sqlite_master "
        "WHERE type = 'table' AND name NOT LIKE 'sqlite_%'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]



def setup_db():
    """
    Creating the database
    If database tables already exist, those are dropped before the creation
    """
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table}")
            db.session.execute(sql)
        db.session.commit()

    print("Creating database")

    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_sql = f.read()

    raw = db.engine.raw_connection()
    try:
        raw.cursor().executescript(schema_sql)
    finally:
        raw.close()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
