from connection import conn


# Add a new book to the database
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    publication_date = input("Enter the publication date of the book (YYYY-MM-DD): ")
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, genre, publication_date) VALUES (%s, %s, %s,%s)", (title, author,genre, publication_date,))
    conn.commit()
    cur.close()


# List all users (admin only)
def list_users(admin_id):
    cur = conn.cursor()
    cur.execute("SELECT id,username,role FROM users WHERE id != %s", (admin_id,))
    rows = cur.fetchall()
    cur.close()
    if not rows:
        print("No users found.")
    else:
        print("ID\tUsername\tRole")
        for row in rows:

            user_id, username, role = row
            print(f"{user_id}\t{username}\t{role}")

# Add a user (admin only)
def add_user():
    # if not is_admin(admin_id):
    #     print("Only administrators can add users.")
    #     return
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match. Please try again.")
        return
    role = input("Enter the role of the user (user or admin): ")
    if role not in ["user", "admin"]:
        print("Invalid role. Please enter 'user' or 'admin'.")
        return
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    if cur.fetchone() is not None:
        print("Username already taken. Please choose another one.")
        return
    cur.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, %s)", (username, password, role))
    conn.commit()
    cur.close()
    print("User added successfully.")

# Promote a user to admin (admin only)
def promote_user(admin_id):
    # if not is_admin(admin_id):
    #     print("Only administrators can promote users.")
    #     return
    user_id = input("Enter the ID of the user you want to promote to admin: ")
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE id = %s AND role = 'user'", (user_id,))
    if cur.fetchone() is None:
        print("Invalid user ID or user is already an admin.")
        return
    cur.execute("UPDATE users SET role = 'admin' WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    print("User promoted to admin successfully.")


#user (admin only)
def demote_admin(admin_id):
    # if not is_admin(admin_id):
    #     print("Only administrators can demote other admins.")
    #     return
    user_id = input("Enter the ID of the admin you want to demote to user: ")
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE id = %s AND role = 'admin'", (user_id,))
    if cur.fetchone() is None:
        print("Invalid user ID or user is not an admin.")
        return
    cur.execute("UPDATE users SET role = 'user' WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    print("Admin demoted to user successfully.")

#Delete a user (admin only)
def delete_user(admin_id):
    # if not is_admin(admin_id):
    #     print("Only administrators can delete users.")
    #     return
    user_id = input("Enter the ID of the user you want to delete: ")
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE id = %s AND role = 'user'", (user_id,))
    if cur.fetchone() is None:
        print("Invalid user ID or user is an admin.")
        return
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    cur.close()
    print("User deleted successfully.")
