class Book:
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('title : ', self.title)
        print('price : ', self.price) 
        print('author : ', self.author) 

    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('new book is bookObject')