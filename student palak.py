import json
import os


class StudentManagement:

    def __init__(self):
        self.filename = "students.json"

        if not os.path.exists(self.filename):
            with open(self.filename, "w") as file:
                json.dump([], file)

    # Read data
    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except Exception:
            return []

    # Save data
    def save_data(self, data):
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Add Student
    def add_student(self):
        data = self.load_data()

        roll = input("Enter Roll Number: ")

        for student in data:
            if student["Roll No"] == roll:
                print("Roll Number already exists.")
                return

        name = input("Enter Name: ")
        course = input("Enter Course: ")

        try:
            marks1 = float(input("Enter Marks of Subject 1: "))
            marks2 = float(input("Enter Marks of Subject 2: "))
            marks3 = float(input("Enter Marks of Subject 3: "))
        except ValueError:
            print("Invalid Marks.")
            return

        total = marks1 + marks2 + marks3
        percentage = total / 3

        student = {
            "Roll No": roll,
            "Name": name,
            "Course": course,
            "Marks1": marks1,
            "Marks2": marks2,
            "Marks3": marks3,
            "Total": total,
            "Percentage": round(percentage, 2)
        }

        data.append(student)
        self.save_data(data)

        print("Student Added Successfully.")

    # View Students
    def view_students(self):
        data = self.load_data()

        if not data:
            print("No Records Found.")
            return

        print("\nStudent Records\n")

        for student in data:
            print(student)
            print("-" * 50)

    # Search Student
    def search_student(self):
        roll = input("Enter Roll Number: ")

        data = self.load_data()

        for student in data:
            if student["Roll No"] == roll:
                print(student)
                return

        print("Student Not Found.")

    # Update Student
    def update_student(self):
        roll = input("Enter Roll Number to Update: ")

        data = self.load_data()

        for student in data:
            if student["Roll No"] == roll:

                student["Name"] = input("Enter New Name: ")
                student["Course"] = input("Enter New Course: ")

                marks1 = float(input("Enter Marks1: "))
                marks2 = float(input("Enter Marks2: "))
                marks3 = float(input("Enter Marks3: "))

                total = marks1 + marks2 + marks3
                percentage = total / 3

                student["Marks1"] = marks1
                student["Marks2"] = marks2
                student["Marks3"] = marks3
                student["Total"] = total
                student["Percentage"] = round(percentage, 2)

                self.save_data(data)

                print("Student Updated Successfully.")
                return

        print("Student Not Found.")

    # Delete Student
    def delete_student(self):
        roll = input("Enter Roll Number to Delete: ")

        data = self.load_data()

        for student in data:
            if student["Roll No"] == roll:
                data.remove(student)
                self.save_data(data)
                print("Student Deleted Successfully.")
                return

        print("Student Not Found.")

    # Menu
    def menu(self):

        while True:

            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            try:
                choice = int(input("Enter Choice: "))

                if choice == 1:
                    self.add_student()

                elif choice == 2:
                    self.view_students()

                elif choice == 3:
                    self.search_student()

                elif choice == 4:
                    self.update_student()

                elif choice == 5:
                    self.delete_student()

                elif choice == 6:
                    print("Thank You!")
                    break

                else:
                    print("Invalid Choice.")

            except ValueError:
                print("Please Enter a Valid Number.")


obj = StudentManagement()
obj.menu()