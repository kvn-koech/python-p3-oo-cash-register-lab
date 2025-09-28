# lib/cash_register.py
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """Add items to the register with optional quantity"""
        self.total += price * quantity
        self.last_transaction = price * quantity
        
        # Add the item title to the items list for each quantity
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """Apply discount to the total and print appropriate message"""
        if self.discount > 0:
            # Calculate discount amount
            discount_amount = self.total * (self.discount / 100)
            # Subtract discount from total
            self.total -= discount_amount
            # Convert to integer if it's a whole number
            if self.total.is_integer():
                self.total = int(self.total)
            # PRINT the success message (not return)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            # PRINT the error message (not return)
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction from the total"""
        self.total -= self.last_transaction
        self.last_transaction = 0
        pass