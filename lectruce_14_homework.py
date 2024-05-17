#Task 1
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Book(Product):
    def __init__(self, name, price, quantity, author):
        super().__init__(name, price, quantity)
        self.author = author

    def read(self):
        print(f"The book '{self.name}' by {self.author} costs ${self.price} each and currently we have {self.quantity} copies in stock.")

try:
    book = Book("1984", 15.99, 10, "George Orwell")
    book.read()
except Exception as e:
    print(f"An error occurred: {e}")


#Task 2
class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu

class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name not in self.menu:
            return f"Sorry, {dish_name} is not available at {self.name}. Please check our menu for available dishes."
        dish = self.menu[dish_name]
        if quantity > dish['quantity']:
            return f"We only have {dish['quantity']} {'units' if dish['quantity'] > 1 else 'unit'} of {dish_name} left. Your requested quantity of {quantity} cannot be fulfilled at the moment."
        dish['quantity'] -= quantity
        total_cost = dish['price'] * quantity
        return f"You have ordered {quantity} {'units' if quantity > 1 else 'unit'} of {dish_name} for a total of ${total_cost}. Thank you for choosing {self.name}!"

menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  
print(mc.order('pizza', 25))  
print(mc.order('soup', 5))  


#Task 3
class Account:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Amount must be positive')

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f'Account number: {self.account_number}, balance: ${self.balance:.2f}'

class SavingsAccount(Account):
    def __init__(self, balance, account_number, interest_rate):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

class CurrentAccount(Account):
    def __init__(self, balance, account_number, overdraft_limit):
        super().__init__(balance, account_number)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount < -self.overdraft_limit:
                print(f'Withdrawal denied. Account {self.account_number} would exceed its overdraft limit: {self.overdraft_limit}.')
            else:
                self.balance -= amount
        else:
            raise ValueError('Amount must be positive')

    def check_overdraft(self):
        if self.balance < 0:
            print(f'Account {self.account_number} is currently in overdraft.')

class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, balance, account_number, account_type, **kwargs):
        if account_type == 'savings':
            new_account = SavingsAccount(balance, account_number, **kwargs)
        elif account_type == 'current':
            new_account = CurrentAccount(balance, account_number, **kwargs)
        self.accounts[account_number] = new_account

    def close_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]

    def pay_dividend(self, amount):
        for account in self.accounts.values():
            account.deposit(amount)

    def update_accounts(self):
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount):
                account.add_interest()
            elif isinstance(account, CurrentAccount):
                account.check_overdraft()

# Test example
bank = Bank()
bank.open_account(0, 1001, 'savings', interest_rate=0.05)
bank.open_account(0, 1002, 'current', overdraft_limit=100)

# Operations and updates
bank.accounts[1001].deposit(1000)  
bank.accounts[1002].deposit(100)   
bank.accounts[1002].withdraw(350) 

# Bank updates
bank.update_accounts()

# Display accounts
for e in bank.accounts.values():
    print(e)

# Close an account
bank.close_account(1002)
