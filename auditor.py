#Vars
stock = 0
user = ""
fails = 0

while user.lower() != "quit":
    user = input("Enter stock quantity: ")
    try:
        if user.lower() == "quit":
            print("Total Units Processed:",stock)
            print("Number of Failed/Rejected Entries:",fails)
            break
        if int(user) >= 0:
            stock = int(user)
            print("Current Stock:",stock)
        else:
            fails += 1
            print("Please enter a positive number.")
    except ValueError:
        fails += 1
        print("Please enter a number.")

    


