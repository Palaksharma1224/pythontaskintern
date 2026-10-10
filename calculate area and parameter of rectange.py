class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    def parameter(self):
        return 2*(self.length+self.width)

res=Rectangle(12,2)

print(res.area(),res.parameter())