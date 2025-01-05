'''
Define a class BankAccount with the following attributes and methods:
Attributes: account_number (string), account_holder (string), balance (float, initialized to 0.0)
Methods:deposit(amount), withdraw(amount) , get_balance()
- Create an instance of BankAccount, - Perform a deposit of $1000, - Perform a withdrawal of $500.
- Print the current balance after each operation.
- Define a subclass SavingsAccount that inherits from BankAccount and adds interest_rate Attribute and
apply_interest() method that Applies interest to the balance based on the interest rate.
And Override print() method to print the current balance and rate.
- Create an instance of SavingsAccount , and call apply_interest() and print() functions. 
'''
# Define a class BankAccount:
class BankAccount:
    def __init__(self, account_number, account_holder, balance = 0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount 
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else: 
            print("you don't have enough money on your balance!")
    def get_balance(self):
        return self.balance
#Create an instance of BankAccount, - Perform a deposit of $1000, - Perform a withdrawal of $500.
instance_1 = BankAccount('25932593', 'Nawar_Atfa')
instance_1.deposit(1000)
print(f"current balance: {instance_1.get_balance()}$") # Print the current balance
instance_1.withdraw(500)
print(f"current balance: {instance_1.get_balance()}$")# Print the current balance

# Define a subclass SavingsAccount that inherits from BankAccount 
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate, balance = 0.0):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate # adds interest_rate Attribute
    
    #define apply_interest() method that Applies interest to the balance based on the interest rate.
    def apply_interest(self): 
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Applied interest of ${interest:.2f}. New balance: ${self.balance:.2f}")
    
    #Override print() method to print the current balance and rate.
    def __str__(self):
        return f"Balance: {self.balance}$, Interest rate: {self.interest_rate}%"

# Create an instance of SavingsAccount: 
instance_2 = SavingsAccount('25932593', 'Nawar_Atfa', 5 )
# Perform a deposit of $1000
instance_2.deposit(1000)
# Apply interest
instance_2.apply_interest()
# Print the current balance and interest rate using the overridden __str__ method
print(instance_2)

        