from device import Device

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device:Device, amount):
        if device.stock >= amount:
            self.items.append({'device': device, 'amount': amount})
            self.total_price += amount * device.price
            device.stock -= amount
            return f'{amount} {device.name} added to cart'
        return f'Not enough stock for {amount} {device.name}'

    def remove_device(self, device:Device, amount):
        for i in self.items:
            if device == i['device']:
                self.items.remove({'device': device, 'amount': amount})
                self.total_price -= amount * device.price
                device.stock += amount
                return f'{amount} {device.name} removed from cart'
        else:
            return f'{device.name} is not in cart'

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device in self.items:
            print(device['device'].name)

    def checkout(self):
        for i in self.items:
            result = f'Your total price is {self.total_price}. Thank you for shopping with us'
            self.remove_device(i['device'], i['amount'])
            return result
        else:
            return 'Your cart is empty'





