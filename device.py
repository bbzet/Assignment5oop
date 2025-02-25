class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        return f'Device name: {self.name}, Price: {self.price}, Stock: {self.stock}, Warranty period: {self.warranty_period}'

    def apply_discount(self, discount_percentage):
        self.price = self.price - (self.price * discount_percentage / 100)
        return self.price

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            return f'{amount} {self.name} removed from stock'
        return f'Not enough stock for {amount} {self.name}'