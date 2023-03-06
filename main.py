import usermenu
import adminmenu
import login_reg
import book

def user_menu(user_id):
    while True:
        print("What would you like to do?")
        print("1. List Books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search")
        print("5. List borrowed books")
        print("6. Logout")
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            book.list_books()
        elif choice == "2":
            usermenu.borrow_book(user_id)
        elif choice == "3":
            usermenu.return_book(user_id)
        elif choice == "4":
            book.search_book()
        elif choice == "5":
            book.list_borrowed()

        elif choice == "6":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(admin_id):
    while True:
        print("What would you like to do?")
        print("1. Add Books")
        print("2. List Books")
        print("3. List borrowed books")
        print("4. List users")
        print("5. Add a user")
        print("6. Promote a user to admin")
        print("7. Demote an admin to user")
        print("8. Delete a user")
        print("9. Logout")
        choice = input("Enter your choice (1-9): ")
        if choice == "1":
            adminmenu.add_book()
        elif choice == "2":
            book.list_books()
        elif choice == "3":
            book.list_borrowed()
        elif choice == "4":
            adminmenu.list_users(admin_id)
        elif choice == "5":
            adminmenu.add_user()
        elif choice == "6":
            adminmenu.promote_user(admin_id)
        elif choice == "7":
            adminmenu.demote_admin(admin_id)
        elif choice == "8":
            adminmenu.delete_user(admin_id)
        elif choice == "9":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice. Please try again.")




# if __name__ == " __main__":
print("Welcome to the Library Management System!")
while True:
        print("What would you like to do?")
        print("1. Register as a new user")
        print("2. Log in")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            login_reg.register()
        elif choice == "2":
            user = login_reg.login()
            if user == None:
                print("Please Try again")
                continue
            user_id, role = user
            if user_id is not None:
                if role == "admin":
                    admin_menu(user_id)
                else:
                    user_menu(user_id)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

