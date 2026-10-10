class Book_details:
    def __init__(self,name,author,publicate,format):
     self.name=name
     self.author=author
     self.publicate=publicate
     self.format=format
    def display(self):
       print("book name",self.name)
       print("book author",self.author)
       print("book publication",self.publicate)
       print("book format",self.format)
book=Book_details("fiarytale","mini moni",2006,"36 volume")
book.display()

