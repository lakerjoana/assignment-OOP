    # Define a class called BankAccount
class BankAccount:
    # Class variable to store the interest rate
    interest_rate = 0.05

    # Constructor to initialize the account holder and balance
    def __init__(self, account_holder, balance=0):
        # Instance variable to store the account holder's name
        self.account_holder = account_holder
        # Instance variable to store the balance (initially set to zero)
        self.balance = balance

    # Method to deposit an amount into the account
    def deposit(self, amount):
        # Add the amount to the balance
        self.balance += amount
        print(f"Deposited ${amount} into {self.account_holder}'s account.")

    # Method to withdraw an amount from the account
    def withdraw(self, amount):
        # Check if there are sufficient funds
        if self.balance >= amount:
            # Subtract the amount from the balance
            self.balance -= amount
            print(f"Withdrew ${amount} from {self.account_holder}'s account.")
        else:
            print("Insufficient funds in the account.")

    # Method to apply interest to the account
    def apply_interest(self):
        # Calculate the interest amount
        interest_amount = self.balance * self.interest_rate
        # Add the interest amount to the balance
        self.balance += interest_amount
        print(f"Applied ${interest_amount} interest to {self.account_holder}'s account.")

    # Method to display the account information
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

# Create two instances of BankAccount with different account holders
account1 = BankAccount("laker joanna")
account2 = BankAccount("laker joanna", 1000)

# Perform a few deposits and withdrawals
account1.deposit(500)
account1.withdraw(200)
account2.deposit(1000)
account2.withdraw(300)

# Apply interest using the apply_interest() method
account1.apply_interest()
account2.apply_interest()

# Display account information for each account
print("Account 1 Information:")
account1.display_account_info()
print("\nAccount 2 Information:")
account2.display_account_info()  
