import os
import pickle
import hashlib
from getpass import getpass

class Account:
    def __init__(self, name, aadhaar, mobile, dob, address, balance=0):
        self.name = name
        self.aadhaar = aadhaar
        self.mobile = mobile
        self.dob = dob
        self.address = address
        self.balance = balance
        self.account_number = None
        self.password = None

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance.")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_data()

    def view_all_accounts(self):
        if self.accounts:
            for acc in self.accounts.values():
                print(f"Account Number: {acc.account_number}, Name: {acc.name}, Balance: {acc.balance}")
        else:
            print("No accounts available.")
    def load_data(self):
        if os.path.exists("accounts.pkl"):
            with open("accounts.pkl", "rb") as f:
                self.accounts = pickle.load(f)

    def save_data(self):
        with open("accounts.pkl", "wb") as f:
            pickle.dump(self.accounts, f)

    def create_account(self, name, aadhaar, mobile, dob, address, initial_deposit):
        account = Account(name, aadhaar, mobile, dob, address, initial_deposit)
        account_number = 1000 + len(self.accounts) + 1
        account.account_number = account_number
        account.password = self.set_password()
        self.accounts[account_number] = account
        self.save_data()
        print(f"Account created successfully. Your account number is {account_number}")

    def set_password(self):
        while True:
            password = getpass("Set a password: ")
            confirm_password = getpass("Confirm your password: ")
            if password == confirm_password:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                return hashed_password
            else:
                print("Passwords do not match. Please try again.")

    def verify_password(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            attempts = 3
            while attempts > 0:
                password = getpass("Enter your password: ")
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                if hashed_password == account.password:
                    return True
                else:
                    attempts -= 1
                    print(f"Incorrect password. {attempts} attempts remaining.")
            return False
        else:
            print("Account not found.")
            return False

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if self.verify_password(account_number):
                self.accounts[account_number].deposit(amount)
                self.save_data()
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.verify_password(account_number):
                self.accounts[account_number].withdraw(amount)
                self.save_data()
        else:
            print("Account not found.")

    def balance_inquiry(self, account_number):
        if account_number in self.accounts:
            if self.verify_password(account_number):
                account = self.accounts[account_number]
                print(f"Account Balance: {account.balance}")
        else:
            print("Account not found.")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            if self.verify_password(account_number):
                del self.accounts[account_number]
                self.save_data()
                print("Account deleted successfully.")
        else:
            print("Account not found.")

class Admin:
    def __init__(self, bank):
        self.bank = bank
        self.username = "admin"
        self.password = hashlib.sha256("admin123".encode()).hexdigest()

    def login(self):
        print("--- Admin Login ---")
        username = input("Enter admin username: ")
        password = getpass("Enter admin password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username == self.username and hashed_password == self.password:
            print("Admin login successful.")
            return True
        else:
            print("Invalid credentials.")
            return False

    def change_password(self):
        if self.login():
            new_password = getpass("Enter new admin password: ")
            self.password = hashlib.sha256(new_password.encode()).hexdigest()
            print("Password changed successfully.")
    def admin_menu(self):
        while True:
            print("\n--- Admin Panel ---")
            print("1. View All Accounts")
            print("2. Delete Account")
            print("3. Exit Admin Panel")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.bank.view_all_accounts()
            elif choice == '2':
                account_number = int(input("Enter account number to delete: "))
                self.bank.delete_account(account_number)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
