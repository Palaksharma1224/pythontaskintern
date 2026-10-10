class Student:
    def __init__(self,name,study,age):
        
          self.name=name
          self.study=study
          self.age=age
    def display(self):
        print("name=",self.name)
        print("study=",self.study)
        print("age=",self.age)

std=Student("palak","BCA",21)
std.display()
