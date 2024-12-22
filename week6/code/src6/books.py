books = []

for i in range(3):
    book = {
        "author": input("Enter an author: "),
        "title": input("Enter a title: ")
    }
    books.append(book)

for book in books:
    print(f"{book['author']} wrote {book['title']}.")
