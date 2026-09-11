#Vars
stock = 0
user = ""

while user.lower() != "quit":
    user = input("Enter stock quantity: ")
    if user != "quit":
        if user.isdigit():
            stock = int(user)
        else:
            print("Please enter a number.")

