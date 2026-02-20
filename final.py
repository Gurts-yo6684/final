



user_name = input("Who are we baking for today? ")

def bakery_options(user_name):
    yessir = input(f"\nWelcome to the Bakery, {user_name}! Would you like to order? (yes/no): ")
    
    order_list = []
    total_cost = []
    
    while yessir.lower() == 'yes':
        sweets = ["1. Cookies", "2. Cinnamon Rolls", "3. Macarons"]
        print(f"\nThank you, {user_name}! What would you like to order?")
        print("\n".join(sweets))
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            cookies = ["1. Macadamia", "2. Chocolate"]
            print("\nToday we have these cookies, please choose one:")
            print("\n".join(cookies))
            cookie_choice = input("Enter the number of the cookie: ")
            
            if cookie_choice == '1':
                order_list.append("Macadamia Cookie")
                total_cost.append(1.50)
                print("Added a Macadamia Cookie to your tray!")
            elif cookie_choice == '2':
                order_list.append("Chocolate Cookie")
                total_cost.append(1.50)
                print("Added a Chocolate Cookie to your tray!")
            else:
                print("Invalid cookie choice.")
                
        elif choice == '2':
            order_list.append("Cinnamon Roll")
            total_cost.append(2.00)
            print("Added Cinnamon Roll to your tray!")
            
        elif choice == '3':
            macarons_choices = ["1. Pistachio", "2. Lemon", "3. Raspberry"]
            print("\nToday we have these macarons, please choose one:")
            print("\n".join(macarons_choices))
            macarons_choice = input("Enter the number of the macaron: ")
            
            if macarons_choice == '1':
                order_list.append("Pistachio Macaron")
                total_cost.append(1.50)
                print("Added a Pistachio Macaron to your tray!")
            elif macarons_choice == '2':
                order_list.append("Lemon Macaron")
                total_cost.append(1.50)
                print("Added a Lemon Macaron to your tray!")
            elif macarons_choice == '3':
                order_list.append("Raspberry Macaron")
                total_cost.append(1.50)
                print("Added a Raspberry Macaron to your tray!")
            else:
                print("Invalid macaron choice.")
        else:
            print("Invalid selection.")
            
        if order_list:
            print(f"\nYour Tray: {', '.join(order_list)}")
            print(f"Current Total: ${sum(total_cost):.2f}")
            
        yessir = input("\nAdd something else? (yes/no): ")
        
    if order_list:
        print(f"\n--- Final Order ---")
        print(f"Items: {', '.join(order_list)}")
        print(f"Final Total: ${sum(total_cost):.2f}")
        print(f"Thanks for stopping by, {user_name}! Enjoy your treats!")
    else:
        print(f"Maybe next time, {user_name}!")

bakery_options(user_name)
