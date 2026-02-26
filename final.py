



user_name = input("Who are we baking for today? ") #User input that is requiered for the parameter

def bakery_options(user_name):   # The function with the parameter that rewuired user input
    yessir = input(f"\nWelcome to the Bakery, {user_name}! Would you like to order? (yes/no): ")
    
    order_list = [] # List number 1 that is going to be motified later in the code
    total_cost = [] # Second list that get modified and changed throughout the code
    
    while yessir.lower() == 'yes': # The while loop that loops around until it is stopped
        sweets = ["1. Cookies", "2. Cinnamon Rolls", "3. Macarons"] # List of sweets
        print(f"\nThank you, {user_name}! What would you like to order?")
        print("\n".join(sweets)) # An addition to the sweets lists
        
        choice = input("Enter the number of your choice: ") # User input is needed
        
        if choice == '1': # An if statement
            cookies = ["1. Macadamia", "2. Chocolate"] # A list named cookies that gives the user a choice
            print("\nToday we have these cookies, please choose one:")
            print("\n".join(cookies)) # A addition to the cookies list
            cookie_choice = input("Enter the number of the cookie: ")
            
            if cookie_choice == '1': # Choice of the user
                order_list.append("Macadamia Cookie")
                total_cost.append(1.50) # Price of what is added
                print("Added a Macadamia Cookie to your tray!")
            elif cookie_choice == '2':
                order_list.append("Chocolate Cookie")
                total_cost.append(1.50) # Price of what is added
                print("Added a Chocolate Cookie to your tray!")
            else:
                print("Invalid cookie choice.")
                
        elif choice == '2':  # Choice of the user and it is a if else stetment
            order_list.append("Cinnamon Roll") # Adds the sweet to the list of what the person ordered
            total_cost.append(2.00) # Price of what is added
            print("Added Cinnamon Roll to your tray!")
            
        elif choice == '3': # Choice of the user and it is a if else stetment
            macarons_choices = ["1. Pistachio", "2. Lemon", "3. Raspberry"]
            print("\nToday we have these macarons, please choose one:")
            print("\n".join(macarons_choices))
            macarons_choice = input("Enter the number of the macaron: ")
            
            if macarons_choice == '1': # Choice of the user
                order_list.append("Pistachio Macaron") # Adds the sweet to the list of what the person ordered
                total_cost.append(1.50) # Price of what is added
                print("Added a Pistachio Macaron to your tray!")
            elif macarons_choice == '2': # If Else statment
                order_list.append("Lemon Macaron") # Adds the sweet to the list of what the person ordered
                total_cost.append(1.50) # Price of what is added
                print("Added a Lemon Macaron to your tray!")
            elif macarons_choice == '3': # If Else statment
                order_list.append("Raspberry Macaron") # Adds the sweet to the list of what the person ordered
                total_cost.append(1.50) # Price of what is added
                print("Added a Raspberry Macaron to your tray!")
            else:
                print("Invalid macaron choice.")
        else:
            print("Invalid selection.")
            
        if order_list:
            print(f"\nYour Tray: {', '.join(order_list)}") # Prints the tray of sweets
            print(f"Current Total: ${sum(total_cost):.2f}") # Adds the total cost of the sweets
            
        yessir = input("\nAdd something else? (yes/no): ") # Gives the user a option of if they want to add soemthing else
        
    if order_list:
        print(f"\n--- Final Order ---")
        print(f"Items: {', '.join(order_list)}") # Prints the tray of sweets
        print(f"Final Total: ${sum(total_cost):.2f}")  # Adds the total cost of the sweets
        print(f"Thanks for stopping by, {user_name}! Enjoy your treats!")
    else:
        print(f"Maybe next time, {user_name}!")

bakery_options(user_name)
