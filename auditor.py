#Vars
stock = 0
user = ""

while user.lower() != "quit":
    user = input("Enter stock quantity: ")
    try:
        if user.lower() == "quit":
            break
        if int(user) >= 0:
            stock = int(user)
            print("Current Stock:",stock)
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a number.")

    


