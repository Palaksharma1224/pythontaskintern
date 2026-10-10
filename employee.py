import json
import os
class employee:
    def __init__(self):
        self.filename="employee.json"
        if not os.path.exists(self.filename):
            with open(self.filename,"w") as file:
                json.dump([],file)

    def load_data(self):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except Exception:
                return []

    def save_data(self,data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_employee(self):
        data=self.load_data()
        emp_id=input("enter employee id")
        try:
                emp_id = int(emp_id)
                if emp_id in data:
                    print("employee id already exists")
                else:
                    name=input("enter employee name")
                    department=input("enter employee department")
                    salary=input("enter employee salary")
                    employee={
                    "emp_id":emp_id,
                    "name":name,
                    "department":department,
                    "salary":salary
                    }
                    print("employee added successfully")
                    data.append(employee)
                    self.save_data(data)
        except ValueError:
            print("Invalid employee id. Please enter a valid integer.")
    def view_employee(self):
        data=self.load_data()
        if not data:
            print("no employee data found")
        else:
            for employee in data:
                print(f"employee id:{employee['emp_id']},name:{employee['name']},department:{employee['department']},salary:{employee['salary']}")

    def search_employee(self):
        data=self.load_data()
        emp_id=input("enter employee id to search")
        try:
            emp_id=int(emp_id)
            for employee in data:
                if employee["emp_id"]==emp_id:
                    print(f"employee id:{employee['emp_id']},name:{employee['name']},department:{employee['department']},salary:{employee['salary']}")
                    return
            print("employee not found")
        except ValueError:
            print("Invalid employee id. Please enter a valid integer.")

    def delete_employee(self):
        data=self.load_data()
        emp_id=input("enter employee id to delete")
        try:
            emp_id=int(emp_id)
            for employee in data:
                if employee["emp_id"]==emp_id:
                    data.remove(employee)
                    self.save_data(data)
                    print("employee deleted successfully")
                    return
            print("employee not found")
        except ValueError:
            print("Invalid employee id. Please enter a valid integer.")

    def update_employee(self):
        data=self.load_data()
        emp_id=input("enter employee id to update")
        try:
            emp_id=int(emp_id)
            for employee in data:
                if employee["emp_id"]==emp_id:
                    name=input("enter new name")
                    department=input("enter new department")
                    salary=input("enter new salary")
                    employee["name"]=name
                    employee["department"]=department
                    employee["salary"]=salary
                    self.save_data(data)
                    print("employee updated successfully")
                    return
            print("employee not found")
        except ValueError:
            print("Invalid employee id. Please enter a valid integer.")

    def calculate_salary(self):
        data=self.load_data()
        emp_id=input("enter employee id to calculate salary")
        try:
            emp_id=int(emp_id)
            for employee in data:
                if employee["emp_id"]==emp_id:
                    expences=200
                    bonus=1000
                    GST=0.18
                    salary=float(employee["salary"])-expences+bonus+(float(employee["salary"])*GST)
                    print(f"employee id:{employee['emp_id']},name:{employee['name']},department:{employee['department']},salary:{salary}",expences=expences,bonus=bonus,GST=GST*100)
                    return
            print("employee not found")
        except ValueError:
            print("Invalid employee id. Please enter a valid integer.")

    def menu(self):
        while True:
            print("1.add employee")
            print("2.view employee")
            print("3.search employee")
            print("4.update employee")
            print("5.calculate salary")
            print("6.delete employee")
            print("7.exit")
            choice=input("enter your choice")
            if choice=="1":
                self.add_employee()
            elif choice=="2":
                self.view_employee()
            elif choice=="3":
                self.search_employee()
            elif choice=="4":
                self.update_employee()
            elif choice=="5":
                self.calculate_salary()
            elif choice=="6":
                self.delete_employee()
            elif choice=="7":
                print("thank you!")
                break
            else:
                print("invalid choice")

emp=employee()
emp.menu()