# PicoVoice-CodingChallenges

## Problem statement #1:
[C, Python]
Assume we have a function get_book_info(isbn) that takes a string ISBN argument and retrieves a
struct/object containing the Title, Author, and Language of a book (each represented as a string) from a database. Write a wrapper function that increases performance by keeping some of the database results in memory for quick lookup.
To prevent memory from growing unbounded, we only want to store a maximum of N book records. At any given time, we should be storing the N books that we accessed most recently. Assume that N can be a large number when making decisions about choices of data structure(s) and algorithm(s).