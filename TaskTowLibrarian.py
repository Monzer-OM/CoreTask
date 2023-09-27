import csv
from typing import List, Dict, Union


# adding the book 
def add_book(title: str, authors: List[str], year: int) -> Dict[str, Union[str, List[str], int]]:
    
    book = {
        "title": title,
        "authors": authors,
        "year": year
    }
    return book

# this function for searching the book 
def search_book(library: List[Dict[str, Union[str, List[str], int]]], title: str) -> Union[Dict[str, Union[str, List[str], int]], None]:
    
    for book in library:
        if book["title"].lower() == title.lower():
            return book
    return None



# this function for loading the books from the csv file
def load_books() -> List[Dict[str, Union[str, List[str], int]]]:
   

    books = []
    try:
        with open('books.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                title = row["title"]
                authors = row["authors"].split(',')
                try:
                    year = int(row["year"])
                except ValueError:
                    print(f"Invalid year format for '{title}': {row['year']}. Skipping this book.")
                    continue
                
                book = add_book(title, authors, year)
                books.append(book)
    except FileNotFoundError:
        raise FileNotFoundError("The 'books.csv' file was not found.")
    except ValueError as e:
        raise ValueError(f"Invalid CSV format or data: {str(e)}")

    return books




library = load_books()
print(library)
    
    # Search for a book by title
search_title = "The Great Gatsby"
found_book = search_book(library, search_title)
    
if found_book:
    print(f"Book found: {found_book['title']} by {', '.join(found_book['authors'])}, Year: {found_book['year']}")
else:
    print(f"Book '{search_title}' not found in the library.")