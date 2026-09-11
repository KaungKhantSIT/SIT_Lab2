#Vars
stock = 0
user = ""

while user.lower() != "quit":
    user = input("Enter stock quantity: ")
    if user != "quit":
        if user.isdigit():
            print("a")
        else:
            print("b")

