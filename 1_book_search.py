"""
Problem statement #1:
[C, Python]
Assume we have a function get_book_info(isbn) that takes a string ISBN argument and retrieves a
struct/object containing the Title, Author, and Language of a book (each represented as a string) from a database. Write a wrapper function that increases performance by keeping some of the database results in memory for quick lookup.
To prevent memory from growing unbounded, we only want to store a maximum of N book records. At any given time, we should be storing the N books that we accessed most recently. Assume that N can be a large number when making decisions about choices of data structure(s) and algorithm(s).
"""

# Solution:
book_memo = {}  # init book_memo: cache for book records, structure {"isbn": book_obj}
isbn_memo = []  # init isbn_memo: cache for isbn records
memo_max_length = 10  # max number of book records to be cached


def book_search(isbn):
    # string isbn. returns a book_obj
    if (isbn not in book_memo) or (book_memo[isbn] == None):
        # try to fetch the book from db
        try:
            book_memo[isbn] = get_book_info(isbn)  # book from db
        except:
            book_memo[isbn] = None  # book unavailable
        if isbn in isbn_memo:
            isbn_memo.remove(isbn)  # remove the previous isbn instance
        isbn_memo.append(isbn)  # add the isbn at the end
        if len(isbn_memo) > memo_max_length:
            # delete the oldest book record
            key_to_remove = isbn_memo.pop(0)  # get and delete the oldest isbn
            book_memo.pop(key_to_remove)  # delete the oldest book record
    return book_memo[isbn]


""" 
# Test:
book_memo = {"1": None}
isbn_memo = ["1"]
memo_max_length = 2


def get_book_info(isbn):
    return "book"


print(book_search("2"), "from db")
print(book_memo, isbn_memo)

print(book_search("1"), "from db")
print(book_memo, isbn_memo)

print(book_search("3"), "from db")
print(book_memo, isbn_memo)

print(book_search("1"), "from cache")
print(book_memo, isbn_memo)
"""

"""
Note: the error handling might need some modifications in real case
"""
