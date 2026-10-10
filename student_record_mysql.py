import mysql.connector as pymysql


class Student_record:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="tiger",
            database="student"
        )
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                rollno INT PRIMARY KEY,
                name TEXT NOT NULL,
                age INT NOT NULL,
                course TEXT NOT NULL,
                science decimal(5,2) NOT NULL,
                maths decimal(5,2) NOT NULL,
                english decimal(5,2) NOT NULL
            )
        """)
        self.connection.commit()
        self.menu()
                   

    def add_student(self):
            try:
                rollno = int(input("Enter roll no: "))
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                course = input("Enter course: ")
                science = float(input("Enter science marks: "))
                maths = float(input("Enter maths marks: "))
                english = float(input("Enter english marks: "))

                self.cursor.execute("""
                INSERT INTO students
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (rollno, name, age, course, science, maths, english))

                self.connection.commit()
                print("Student added successfully.")

            except:
                print("This roll number already exists.")
    

    def view_students(self):

        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()

        if not students:
            print("No students available.")
            return

        for student in students:
            total = student[4] + student[5] + student[6]
            percentage = total / 300 * 100

            print("\n===== Student Details =====")
            print("Roll no:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Science:", student[4])
            print("Maths:", student[5])
            print("English:", student[6])
            print("Total:", total)
            print("Percentage:", round(percentage, 2), "%")

    def search_student(self):
        rollno = int(input("Enter roll no to search: "))

        self.cursor.execute("SELECT * FROM students WHERE rollno = %s", (rollno,))
        student = self.cursor.fetchone()

        if student:
            print("\n===== Student Found =====")
            print("Roll no:", student[0])
            print("Name:", student[1])
            print("Age:", student[2])
            print("Course:", student[3])
            print("Science:", student[4])
            print("Maths:", student[5])
            print("English:", student[6])
        else:
            print("Student not found.")

    def update_student(self):
        rollno = int(input("Enter roll no to update: "))

        self.cursor.execute(
            "SELECT * FROM students WHERE rollno = ?",
            (rollno,)
        )

        if not self.cursor.fetchone():
            print("Student not found.")
            return

        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        course = input("Enter new course: ")
        science = float(input("Enter new science marks: "))
        maths = float(input("Enter new maths marks: "))
        english = float(input("Enter new english marks: "))

        self.cursor.execute("""
            UPDATE students
            SET name = %s, age = %s, course = %s, science = %s, maths = %s, english = %s
            WHERE rollno = %s
        """, (name, age, course, science, maths, english, rollno))

        self.connection.commit()
        print("Student updated successfully.")

    def delete_student(self):
        rollno = int(input("Enter roll no to delete: "))

        self.cursor.execute(
            "DELETE FROM students WHERE rollno = %s",
            (rollno,)
        )
        self.connection.commit()

        if self.cursor.rowcount > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def display_topper(self):
        self.cursor.execute("""
            SELECT * FROM students
            ORDER BY (science + maths + english) DESC
            LIMIT 1
        """)
        topper = self.cursor.fetchone()

        if topper:
            total = topper[4] + topper[5] + topper[6]
            percentage = total / 300 * 100

            print("\n===== Topper Details =====")
            print("Name:", topper[1])
            print("Roll no:", topper[0])
            print("Total:", total)
            print("Percentage:", round(percentage, 2), "%")
        else:
            print("No students available.")

    def display_average_percentage(self):
        self.cursor.execute("""
            SELECT AVG((science + maths + english) / 300.0 * 100)
            FROM students
        """)
        average = self.cursor.fetchone()[0]

        if average is not None:
            print("Average percentage:", round(average, 2), "%")
        else:
            print("No students available.")
    def menu(self):
        while True:
                print("\n===== Student Management System =====")
                print("1. Add Student")
                print("2. View Students")
                print("3. Search Student")
                print("4. Update Student")
                print("5. Delete Student")
                print("6. Display Topper")
                print("7. Display Average Percentage")
                print("8. Exit")
                    
                choice = input("Enter your choice (1-8): ")
                    
                match choice:
                            case "1":
                                self.add_student()
                            case "2":
                                    self.view_students()
                            case "3":
                                    self.search_student()
                            case "4":
                                    self.update_student()
                            case "5":
                                    self.delete_student()
                            case "6":
                                    self.display_topper()
                            case "7":
                                    self.display_average_percentage()
                            case "8":
                                    print("Program ended.")
                                    self.connection.close()
                                    break
                            case _:
                                    print("Enter a valid number.")

student_details = Student_record()