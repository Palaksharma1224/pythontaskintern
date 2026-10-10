class Student_details:
    def __init__(self,name,study,age,marks):
        self.name=name
        self.study=study
        self.age=age
        self.marks=marks
    
    def display(self):
        print("name:",self.name)
        print("study",self.study)
        print("age",self.age)
        print("marks",self.marks)

    def percentage(self):
        percent=(self.marks/200)*100
        print( percent)       

std=Student_details("navya","bca",21,170)
std.display()
std.percentage()

