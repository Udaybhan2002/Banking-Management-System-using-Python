from bank import Bank

def user_interface(bank):
    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Balance Inquiry")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            aadhaar = input("Enter your Aadhaar number: ")
            mobile = input("Enter your mobile number: ")
            dob = input("Enter your date of birth (YYYY-MM-DD): ")
            address = input("Enter your address: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                continue
            
            bank.create_account(name, aadhaar, mobile, dob, address, initial_deposit)
        
        elif choice == 2:
            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(account_number, amount)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        
        elif choice == 3:
            try:
                account_number = int(input("Enter your account number: "))
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(account_number, amount)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        
        elif choice == 4:
            try:
                account_number = int(input("Enter your account number: "))
                bank.balance_inquiry(account_number)
            except ValueError:
                print("Invalid input. Please enter a valid account number.")
        
        elif choice == 5:
            print("Thank you for using MyBank. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")