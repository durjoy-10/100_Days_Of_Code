# Write a library class with no_of_books and books as two instance variables.Write a program to create a library
# from this Library class and show how can print all books,add a book and get the number of books using different
# methods.Show that your program doesnot presist the books after the program is stopped!

class Library:
    def __init__(self):
        self.noBooks=0
        self.books=[]
        
    def addbook(self,book):
        self.books.append(book)
        self.noBooks=len(self.books)
        
    def showInfo(self):
        print(f"The library has {self.noBooks}. The books are-")
        for book in self.books:
            print(book)
            
l1=Library()
l1.addbook("Harry Potter1")
l1.addbook("Harry Potter2")
l1.addbook("Harry Potter3")
l1.addbook("Harry Potter4")
add=int(input("If you want to show how many books already in the library then press 0\nAnd if you want to add more books then press 1:\n "))
if(add==1):
    num=int(input("How many books you want to added:"))
    for num in range(0,num):
        print("add",num+1,"book name:")
        bookName=input()
        l1.addbook(bookName)
    l1.showInfo()
else:
    l1.showInfo()