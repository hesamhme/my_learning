from my_library import Library

def main():
    library = Library()
    while True:
        print("\nمدیریت کتابخانه:")
        print("1. اضافه کردن کتاب")
        print("2. حذف کتاب")
        print("3. جستجوی کتاب")
        print("4. نمایش همه‌ی کتاب‌ها")
        print("5. خروج")

        choice = input("انتخاب کنید: ")

        if choice == '1':
            title = input("عنوان کتاب: ")
            author = input("نویسنده: ")
            library.add_book(title, author)
        elif choice == '2':
            title = input("عنوان کتاب: ")
            library.remove_book(title)
        elif choice == '3':
            title = input("عنوان کتاب: ")
            library.search_book(title)
        elif choice == '4':
            library.show_books()
        elif choice == '5':
            print("خروج از برنامه...")
            break
        else:
            print("گزینه نامعتبر است.")

if __name__ == "__main__":
    main()
