### Exercise 1 - Turn the shopping cart program from last week into an object-oriented program

# The comments in the cell below are there as a guide for thinking about the problem. 
# However, if you feel a different way is best for you and your own thought process, 
# please do what feels best for you by all means.



class Shopping_cart():
    def __init__(self):
        self.cart  = {}

    def add(self):
        item = input("What would you like to add to your cart? ")
        quan = input("How many? ")
        self.cart[item] = quan
        print(f"{item} has been added  to your cart.")

    def show(self):
        print(self.cart)
    
    def delete(self):
        item = input("What item  would you like to delete? ")
        del self.cart[item]
        print(f'You have deleted {item} from your cart')

    def run(self):
        while True:
            menu = input("Welcome to my  shop!  Show/Add/Delete or Quit?  ")
            
            if menu.lower() == "quit":
                self.show()
                break

            elif menu.lower()  ==  "add":
                self.add()
            
            elif menu.lower() == "show":
                self.show()

            elif menu.lower() == "delete":
                self.delete()

i = Shopping_cart()   
i.run()     


### Exercise 2 - Write a Python class which has two methods get_String and print_String. 
# get_String accept a string from the user and print_String print the string in upper case

class BigString:
    def __init__(self):
        self.my_string = ""

    def get_string(self):
        self.my_string = input("Please enter your string: ")

    def print_string(self):
        print(self.my_string.upper())


i = BigString()
i.get_string()
i.print_string()
