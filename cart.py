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
        if device in self.items:
            if self.items.count(device) >= amount:
                self.items.remove(device)
                self.total_price -= amount * device.price
                device.stock += amount
            else:
                return f'Not enough {device.name} in cart'
        else:
            return f'{device.name} not in cart'

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device in self.items:
            print(device.name)

    def checkout(self):
        for device in self.items:
            self.remove_device(device, self.items.count(device))
        return f'Your total price is {self.total_price}. Thank you for shopping with us'




