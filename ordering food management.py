import sqlite3

class restaurent:
    cart=[]
    def __init__(self):
        self.connection=sqlite3.connect("order.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders(
            ELEMENTS VARCHAR(20),
            PRICE FLOAT
            )
            """)
        self.connection.commit()
        self.menu_details()
       
    def menu(self):
            self.menu={
                "pizza":199,
                "pasta":50,
                "noodles":80,
                "panner tikka":190,
                "manchurian":80,
                "momos":50,
                "burger":40
            }
            print("\n----- MENU -----")
            for item, price in self.menu.items():
                print(f"{item} \t ₹{price}")

    def add_items(self):
            food = input("Enter food name: ")
         
            if food in self.menu:
                self.cart.append(food)
                print(food, "added to cart.")
            else:
                print("Sorry! Item not available.")

    def  view_cart(self):
            if len(self.cart) == 0:
                print("Your cart is empty.")
            elif  len(self.cart)>0:
                print("\n----- YOUR CART -----")
                for food in self.cart:
                    print(food)

            else:
                 print("your cart is empty")
                    
              
    def remove_item(self):
        item=input("enter the item to remove from cart")
        if item in self.cart:
            self.cart.remove(item)
            print(item,"remove from cart")
        else:
            print("item is not in cart")

    def discount(self):
            total=0
            while True:
                print("======discount section=====")
                print("1.student 5%")
                print("2.adult 7%")
                print("3.worker 0%")

                choice=int(input("enter the number"))
                
                for item in self.cart:
                    if choice==1:
                        total += self.menu[item]
                        discount = total*5/100
                        total-= discount
                        print(f"discount credited{discount}")

                        break
                    elif choice==2:
                        total += self.menu[item]
                                            
                        discount =total*7/100
                        total-=discount
                        print(f"discount credited{discount}")
                        break

                    elif choice==3:
                        print("no discount is being there for the worker ")

                        break
                    else:
                        print("invalid choice")
                break
                    

    def bill_generation(self):
        if len(self.cart) == 0:
                print("Your cart is empty.")
        else:
            print("\n----- BILL -----")
            total = 0
            for item in self.cart:
                total += self.menu[item]
                gst = total * 18 / 100
                grand_total = total + gst
                print(f"{item} \t ₹{self.menu[item]}")
                print("-----------------------")
                print("Total      :", total)
                print("GST (18%)  :", gst)
                print("Grand Total:", grand_total)
        
               
            


    def per_plate(self):
        food = input("Enter food name: ")

        if food in self.menu:
            plates = int(input("Enter number of plates: "))
            cost = self.menu[food] * plates
            print("Cost =", cost)
        else:
            print("Food not available")

    def menu_details(self):
            while True:
                    print("\n===== food ordering =====")
                    print("1. view  food items")
                    print("2. add item ")
                    print("3.  view cart")
                    print("4. remove item")
                    print("5. bill generation")
                    print("6. discount")
                    print("7. bill per palte")
                    print("8. Exit")
                        
                    choice = input("Enter your choice (1-8): ")
                        
                    match choice:
                        case "1":
                            self.menu()
                        case "2":
                                self.add_items()
                        case "3":
                              self. view_cart() 
                        case "4":
                                self.remove_item()
                        case "5":
                                self.bill_generation()
                        case "6":
                                self.discount()
                        case "7":
                                self.per_plate()
                        case "8":
                                print("Program ended.")
                                self.connection.close()
                                break
                        case _:
                            print("Enter a valid number.")


management= restaurent()
