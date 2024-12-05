class Book:
    def __init__(self, title, author, price, pages):
        # Attributes
        self.title = title
        self.author = author
        self.__price = price  # Private attribute 
        self.pages = pages

    # accessing the private attribute 
    def get_price(self):
        return self.__price

    # applying discount to the price 
    def apply_discount(self, discount_percentage):
        discount_amount = self.__price * (discount_percentage / 100)
        self.__price -= discount_amount
        print(f"The price after {discount_percentage}% discount is: ${self.__price:.2f}")

    # reading a page 
    def read_page(self, page_number):
        if 1 <= page_number <= self.pages:
            print(f"Reading page {page_number} of '{self.title}'...")
        else:
            print("Invalid page number.")

    # a method to display the book information 
    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPrice: ${self.__price:.2f}\nPages: {self.pages}"

class EBook(Book):
    def __init__(self, title, author, price, pages, file_format):
        super().__init__(title, author, price, pages)
        self.file_format = file_format  

    # Overriding method to read a page for EBook
    def read_page(self, page_number):
        if 1 <= page_number <= self.pages:
            print(f"Opening page {page_number} of the {self.file_format} version of '{self.title}'...")
        else:
            print("Invalid page number for the EBook.")

    # Overriding the display_info method to include file format
    def display_info(self):
        base_info = super().display_info()  # Get base class info
        return f"{base_info}\nFile Format: {self.file_format}"

# instances of classes
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 15.99, 180)
ebook1 = EBook("Digital Fortress", "Dan Brown", 9.99, 350, "PDF")

# Interacting with the objects
print(book1.display_info())  # Show information of the physical book
book1.apply_discount(10)  # Applying 10% discount
book1.read_page(50)

print("\n" + ebook1.display_info())  # Show information for the Ebook
ebook1.apply_discount(20)  # Applying 20% discount
ebook1.read_page(50)
