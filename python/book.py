import csv
import datetime
import re

class Book:
    def __init__(self, book_id, type, copies, title, author, year, keywords):
        self.book_id = book_id
        self.type = type
        self.copies = copies
        self.title = title
        self.author = author
        self.year = year
        self.keywords = keywords
    def __str__(self):
        return (f"book_id:{self.book_id}, type:{self.type}, copies:{self.copies}, title:{self.title},author:{self.author}, year:{self.year},keywords:{self.keywords}")
def load_books(books_file: str) -> list:
    books = []
    with open(books_file, "r", encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
           
            books.append({'book_id': row['book_id'],
                'type': row['type'],
                'copies': int(row['copies']),
                'title': row['title'],
                'author': row['author'],
                'year': row['year'],
                'keywords': row['keywords']})
            
    return books