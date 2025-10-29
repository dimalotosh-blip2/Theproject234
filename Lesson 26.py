import sqlite3

sql_script = """
CREATE TABLE Animals (Nazva_Zvіra TEXT, Typ_Zvіra TEXT);

INSERT INTO Animals (Nazva_Zvіra, Typ_Zvіra)
VALUES
    ('Лев', 'Ссавець'),
    ('Крокодил', 'Плазун'),
    ('Орел', 'Птах'),
    ('Морська черепаха', 'Плазун'),
    ('Мавпа', 'Ссавець');

UPDATE Animals SET Nazva_Zvіra = 'Сокіл' WHERE Nazva_Zvіra = 'Орел';
"""

with sqlite3.connect(':memory:') as conn:
    c = conn.cursor()
    
    c.executescript(sql_script)

    print("--- Ссавці ---")
    c.execute("SELECT * FROM Animals WHERE Typ_Zvіra = 'Ссавець'")
    print(c.fetchall())

    print("\n--- Всі звірі ---")
    c.execute("SELECT * FROM Animals")
    print(c.fetchall())