class Library:
    def __init__(self,books):
        self.books=books

    def list_books(self):
        print("Available Books")
        for i in self.books:
            print(i)
    def borrow_book(self,borrow_book):
        if borrow_book in self.books:
            print("Get your Book Now")
            self.books.remove(borrow_book)
    def return_book(self,return_book):
        print("you have returned the book")
        self.book.append(return_book)
books = ['C','C++','Python','Java']
o=Library(books)
msg="""
    Enter 1 >>> For Display Books
    Enter 2 >>> For Borrow Books
    Enter 3 >>> For Returning Books
"""
while(True):
    print(msg)
    ch= int(input("Enter Your Choice: "))
    if ch==1:
        o.list_books()
    elif ch==2:
        book=input("Enter book name to Borrow: ")
        o.borrow_book(book)
    elif ch==3:
        book = input("Enter book name to Return: ")
        o.return_book(book)
    else:
        print("thank you!")
        quit()