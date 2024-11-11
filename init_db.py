import sqlite3

def init_db():
    # Vytvoření připojení k databázi (vytvoří soubor, pokud neexistuje)
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Vytvoření tabulky users
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            name VARCHAR(100),
            is_active BOOLEAN DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Uložení změn a uzavření spojení
    conn.commit()
    conn.close()
    print("Databáze byla úspěšně vytvořena.")

if __name__ == '__main__':
    init_db()