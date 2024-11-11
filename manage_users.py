import sqlite3
import hashlib

def create_user(username, password, name):
    conn = sqlite3.connect('database.db')
    # Vytvoření hash hesla
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    try:
        conn.execute('INSERT INTO users (username, password_hash, name) VALUES (?, ?, ?)',
                    (username, password_hash, name))
        conn.commit()
        print(f"Uživatel {username} byl úspěšně vytvořen")
    except sqlite3.IntegrityError:
        print(f"Uživatel {username} již existuje")
    finally:
        conn.close()

def list_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT username, name, is_active FROM users')
    users = cursor.fetchall()
    print("\nSeznam uživatelů:")
    print("Username | Jméno | Aktivní")
    print("-" * 40)
    for user in users:
        print(f"{user[0]} | {user[1]} | {'Ano' if user[2] else 'Ne'}")
    conn.close()

if __name__ == '__main__':
    while True:
        print("\nSpráva uživatelů")
        print("1. Vytvořit nového uživatele")
        print("2. Zobrazit seznam uživatelů")
        print("3. Konec")
        
        choice = input("Vyberte akci (1-3): ")
        
        if choice == "1":
            username = input("Zadejte uživatelské jméno: ")
            password = input("Zadejte heslo: ")
            name = input("Zadejte celé jméno: ")
            create_user(username, password, name)
        elif choice == "2":
            list_users()
        elif choice == "3":
            break
        else:
            print("Neplatná volba")