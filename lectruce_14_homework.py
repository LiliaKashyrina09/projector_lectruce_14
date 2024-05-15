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

# Example usage:
menu = {
    'burger': {'price': 5, 'quantity': 10},
    'pizza': {'price': 10, 'quantity': 20},
    'drink': {'price': 1, 'quantity': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  
print(mc.order('pizza', 25))  
print(mc.order('soup', 5))  

       
