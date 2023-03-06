from datetime import date
from connection import conn

# Borrow a book
def borrow_book(user_id):
    book_id = input("Enter the ID of the book you want to borrow: ")
    cur = conn.cursor()
    cur.execute("SELECT available FROM books WHERE id = %s", (book_id,))
    row = cur.fetchone()
    if not row:
        print("Book not found.")
        return
    available = row[0]
    if not available:
        print("Book is not available.")
        return
    cur.execute("UPDATE books SET available = FALSE WHERE id = %s", (book_id,))
    loan_date = str(date.today())
    cur.execute("INSERT INTO loans (book_id, borrower_id, loan_date) VALUES (%s, %s, %s)", (book_id, user_id, loan_date))
    conn.commit()
    cur.close()

# Return a book
def return_book(user_id):
    book_id = input("Enter the ID of the book you want to return: ")
    cur = conn.cursor()
    cur.execute("SELECT borrower_id, loan_date, return_date FROM loans WHERE book_id = %s AND return_date IS NULL", (book_id,))
    row = cur.fetchone()
    if not row:
        print("Book not found.")
        return
    borrower_id, loan_date, return_date = row
    if user_id != borrower_id:
        print("You did not borrow this book.")
        return
    cur.execute("UPDATE books SET available = TRUE WHERE id = %s", (book_id,))
    return_date = str(date.today())
    cur.execute("UPDATE loans SET return_date = %s WHERE book_id = %s AND borrower_id = %s", (return_date, book_id, borrower_id))
    conn.commit()
    cur.close()


