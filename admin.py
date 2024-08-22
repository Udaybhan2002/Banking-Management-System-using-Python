from bank import Admin
def admin_interface(bank):
    admin = Admin(bank)
    
    if admin.login():
        while True:
            print("\n--- Admin Panel ---")
            print("1. admin_menu")
            print("2. Change Admin Password")
            print("3. Exit Admin Panel")
            try:
                admin_choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if admin_choice==1:
                admin.admin_menu()
            elif admin_choice == 2:
                admin.change_password()
            elif admin_choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")
