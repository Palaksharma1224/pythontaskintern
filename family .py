import json
import os
class FamilyMember:
    def __init__(self):
        self.filename="family members.json"
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


    def add_member(self, member):
        data=self.load_data()
        member_id=member.get("member_id")
        if any(m["member_id"] == member_id for m in data):
            print("Member ID already exists")
        else:
            data.append(member)
            self.save_data(data)
            print("Family member added successfully")

    def view_members(self,member):
        data=self.load_data()
        if not data:
            print("No family member data found")
        else:
            for member in data:
                print(f"Member ID: {member['member_id']}, Name: {member['name']}, Age: {member['age']}, Relationship: {member['relationship']}")

    def check_adhar(self,member):
        data=self.load_data()
        adhar_number=input("Enter Aadhar number to check: ")
        for member in data:
            if member.get("adhar_number") == adhar_number:
                print(f"Member ID: {member['member_id']}, Name: {member['name']}, Age: {member['age']}, Relationship: {member['relationship']}")
                return
        print("Aadhar number not found")

    def search_member(self,member):
        data=self.load_data()
        member_id=input("Enter member ID to search: ")
        try:
            member_id=int(member_id)
            for member in data:
                if member["member_id"]==member_id:
                    print(f"Member ID: {member['member_id']}, Name: {member['name']}, Age: {member['age']}, Relationship: {member['relationship']}")
                    return
            print("Family member not found")
        except ValueError:
            print("Invalid member ID. Please enter a valid integer.")

    def delete_member(self,member):
        data=self.load_data()
        member_id=input("Enter member ID to delete: ")
        try:
            member_id=int(member_id)
            for i, member in enumerate(data):
                if member["member_id"]==member_id:
                    del data[i]
                    self.save_data(data)
                    print("Family member deleted successfully")
                    return
            print("Family member not found")
        except ValueError:
            print("Invalid member ID. Please enter a valid integer.")

    def menu(self):
        while True:
            print("1.add member")
            print("2.view member")
            print("3.search member")
            print("4.delete member")
            print("5.check adhar")
            print("6.exit")
            choice=input("enter your choice")
            if choice=="1":
                    self.add_member()
            elif choice=="2":
                            self.view_members()
            elif choice=="3":
                            self.search_member()
            elif choice=="4":
                            self.delete_member()
            elif choice=="5":
                            self.check_adhar()
            elif choice=="6":
                            print("thank you!")
                            break
            else:
                            print("invalid choice")
            
FamilyMember=FamilyMember()
FamilyMember.menu()