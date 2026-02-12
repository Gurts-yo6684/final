


def bakery_options():
    yessir = input("Welcome to the Bakery! Would you like to order something? (yes/no): ")
    while yessir.lower() == 'yes':
        name = input("To whom is this order for? ")
        
        sweets = ["1. Cookies", "2. Cinnamon Rolls", "3. Macarons", "4. Pastry of the day"]
        order_list = []
        total_cost = []
        
        print(f"\nThank you, {name}! What would you like to order?")
        print("\n".join(sweets))
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            cookies = ["1. Macadamia", "2. Chocolate"]
            print("\nToday we have these cookies, please choose one:")
            print("\n".join(cookies))
            cookie_choice = input("Enter the number of the cookie: ")
            
            if cookie_choice == '1':
                order_list.append("Macadamia Cookie")
                total_cost.append("1.50")
                print("Added a Macadamia Cookie to your tray!")
            elif cookie_choice == '2':
                order_list.append("Chocolate Cookie")
                print("Added a Chocolate Cookie to your tray!")
            else:
                print("Invalid cookie choice.")
                
        
        print(f"\nYour current order: {order_list}")
        print(f"\nThe total cost is:",{total_cost})

        yessir = input("\nWould you like to make another order? (yes/no): ")

    print("Thank you for visiting the bakery! Goodbye.")


bakery_options()

# (1) cookie (macademia, choclate)
# (2) cinammon roll
# (3) macarons (pistachio, lemon, raspberry)
# (4) pastry of the day (from random list of flavors (7))
