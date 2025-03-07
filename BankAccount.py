class BankAccount:
    accounts = []  

    def _init_(self, account_number, account_type, account_holder, initial_balance):
        self.account_number = account_number
        self.account_type = account_type
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []  
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: ₹{amount}")
            print(f"₹{amount} deposited successfully. New Balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if self.account_type == "Savings" and amount > self.balance:
            print("Insufficient funds! No overdraft allowed for Savings account.")
        elif self.account_type in ["Current", "Business"] and (self.balance - amount) < -10000:
            print("Overdraft limit reached! Cannot withdraw this amount.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: ₹{amount}")
            print(f"₹{amount} withdrawn successfully. New Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Account Balance: ₹{self.balance}")

    def transaction_history(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    @staticmethod
    def find_account(account_number):
        for account in BankAccount.accounts:
            if account.account_number == account_number:
                return account
        return None

# Admin Functions
def create_account():
    account_number = input("Enter Account Number: ")
    if BankAccount.find_account(account_number):
        print("Account number already exists! Please use a unique number.")
        return

    account_type = input("Enter Account Type (Savings/Current/Business): ")
    if account_type not in ["Savings", "Current", "Business"]:
        print("Invalid account type!")
        return

    account_holder = input("Enter Account Holder Name: ")
    initial_balance = float(input("Enter Initial Balance: "))

    # Enforce minimum balance rules
    if (account_type == "Savings" and initial_balance < 1000) or \
       (account_type == "Current" and initial_balance < 5000):
        print(f"Initial balance too low for {account_type} account!")
        return

    BankAccount(account_number, account_type, account_holder, initial_balance)
    print(f"Account created successfully for {account_holder}!")

# Customer Functions
def deposit_money():
    account_number = input("Enter Account Number: ")
    account = BankAccount.find_account(account_number)
    if not account:
        print("Account not found!")
        return

    amount = float(input("Enter Deposit Amount: "))
    account.deposit(amount)

def withdraw_money():
    account_number = input("Enter Account Number: ")
    account = BankAccount.find_account(account_number)
    if not account:
        print("Account not found!")
        return

    amount = float(input("Enter Withdrawal Amount: "))
    account.withdraw(amount)

def check_balance():
    account_number = input("Enter Account Number: ")
    account = BankAccount.find_account(account_number)
    if not account:
        print("Account not found!")
        return

    account.check_balance()

def view_transaction_history():
    account_number = input("Enter Account Number: ")
    account = BankAccount.find_account(account_number)
    if not account:
        print("Account not found!")
        return

    account.transaction_history()

# Main Menu
def main():
    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. View Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            check_balance()
        elif choice == "5":
            view_transaction_history()
        elif choice == "6":
            print("Exiting... Thank you for using the banking system!")
            break
        else:
            print("Invalid choice! Please try again.")


#if __name__ == "_main_":
    main()