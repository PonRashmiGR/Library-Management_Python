import getpass
from connection import conn

# Login function
def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    cur = conn.cursor()
    cur.execute("SELECT id, role FROM users WHERE username = %s AND password = %s", (username, password))
    row = cur.fetchone()
    cur.close()
    if not row:
        print("Invalid username or password.")
        return None
    user_id, role = row
    return (user_id, role)

# Register function
def register():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    if cur.fetchone() is not None:
        print("Username already taken. Please choose another one.")
        return
    cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, "user"))
    conn.commit()
    cur.close()
    print("Registration successful.")