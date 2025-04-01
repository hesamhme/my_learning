class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append({'title': title, 'author': author})
        print(f'کتاب "{title}" توسط "{author}" اضافه شد.')

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                print(f'کتاب "{title}" حذف شد.')
                return
        print(f'کتاب "{title}" یافت نشد.')

    def search_book(self, title):
        for book in self.books:
            if book['title'] == title:
                print(f'کتاب یافت شد: "{title}" توسط "{book["author"]}"')
                return
        print(f'کتاب "{title}" یافت نشد.')

    def show_books(self):
        if not self.books:
            print("هیچ کتابی موجود نیست.")
        for book in self.books:
            print(f'کتاب: "{book["title"]}", نویسنده: "{book["author"]}"')
