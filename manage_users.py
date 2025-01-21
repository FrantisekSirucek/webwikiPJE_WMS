import sqlite3
import hashlib

def create_user(username, password, name):
    conn = sqlite3.connect('database.db')
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

def change_password(username, new_password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Nejprve ověříme, zda uživatel existuje
    cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    
    if user is None:
        print(f"Uživatel {username} neexistuje")
        conn.close()
        return
    
    try:
        # Vytvoření hash nového hesla
        new_password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        
        # Aktualizace hesla
        cursor.execute('UPDATE users SET password_hash = ? WHERE username = ?',
                      (new_password_hash, username))
        conn.commit()
        print(f"Heslo pro uživatele {username} bylo úspěšně změněno")
    except Exception as e:
        print(f"Chyba při změně hesla: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    while True:
        print("\nSpráva uživatelů")
        print("1. Vytvořit nového uživatele")
        print("2. Zobrazit seznam uživatelů")
        print("3. Změnit heslo uživatele")
        print("4. Konec")
        
        choice = input("Vyberte akci (1-4): ")
        
        if choice == "1":
            username = input("Zadejte uživatelské jméno: ")
            password = input("Zadejte heslo: ")
            name = input("Zadejte celé jméno: ")
            create_user(username, password, name)
        elif choice == "2":
            list_users()
        elif choice == "3":
            username = input("Zadejte uživatelské jméno: ")
            new_password = input("Zadejte nové heslo: ")
            change_password(username, new_password)
        elif choice == "4":
            break
        else:
            print("Neplatná volba")