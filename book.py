from connection import conn

# List all books in the database
def list_books():
    cur = conn.cursor()
    cur.execute("SELECT id, title, author, genre, publication_date, available FROM books")
    rows = cur.fetchall()
    cur.close()
    if not rows:
        print("No books found.")
    else:
        print("ID\tTitle\tAuthor\tgenre\tPublication Date\tAvailable")
        for row in rows:
            book_id, title, author, genre, publication_date, available = row
            print(f"{book_id}\t{title}\t{author}\t{genre}\t{publication_date}\t{available}")

def list_borrowed():
    cur = conn.cursor()
    cur.execute("SELECT loans.book_id, books.title, users.username, loans.loan_date, loans.return_date FROM loans JOIN books ON loans.book_id = books.id JOIN users ON loans.borrower_id = users.id WHERE loans.return_date IS NULL")
    rows = cur.fetchall()
    cur.close()
    if not rows:
        print("No borrowed books found.")
    else:
        print("Book ID\tTitle\tBorrower\tLoan Date\tReturn Date")
        for row in rows:
            book_id, title, borrower, loan_date, return_date = row
            print(f"{book_id}\t{title}\t{borrower}\t{loan_date}\t{return_date}")

# Function to search for a book by title or author
def search_book():
    search = input("Enter search term: ")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, genre publication_date, available FROM books WHERE title LIKE %s OR author LIKE %s",('%' + search + '%', '%' + search + '%'))
    results = cursor.fetchall()
    cursor.close()
    if not results:
        print("No results found")
    else:
        print("ID\tTitle\tAuthor\tPublication Date\tAvailable")
        for row in results:
            book_id, title, author, publication_date, available = row
            print(f"{book_id}\t{title}\t{author}\t{publication_date}\t{available}")
