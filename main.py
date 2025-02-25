from device import Device
from laptop import Laptop
from smartphone import Smartphone
from tablet import Tablet
from cart import Cart

devices = [
    Smartphone("iPhone 13", 999, 10, 12, 6.1, 20),
    Smartphone("Samsung Galaxy S21", 799, 15, 12, 6.2, 22),
    Laptop("MacBook Pro", 1299, 5, 24, 16, 3.2),
    Laptop("Dell XPS 13", 999, 8, 24, 8, 2.8),
    Tablet("iPad Pro", 799, 12, 12, 12.9, 10),
    Tablet("Samsung Galaxy Tab S7", 649, 10, 12, 11, 14),
    Smartphone("Google Pixel 6", 599, 20, 12, 6.4, 24),
    Laptop("HP Spectre x360", 1099, 7, 24, 16, 3.0),
    Tablet("Microsoft Surface Pro 7", 749, 9, 12, 12.3, 13),
    Smartphone("OnePlus 9", 729, 18, 12, 6.55, 23),
    Laptop("Lenovo ThinkPad X1", 1199, 6, 24, 16, 3.1),
    Tablet("Amazon Fire HD 10", 149, 25, 12, 10.1, 12),
    Smartphone("Sony Xperia 5 II", 949, 11, 12, 6.1, 21),
    Laptop("Asus ZenBook 14", 899, 10, 24, 16, 2.9),
    Tablet("Lenovo Tab P11 Pro", 499, 14, 12, 11.5, 15),
    Smartphone("Xiaomi Mi 11", 749, 17, 12, 6.81, 22),
    Laptop("Acer Swift 3", 699, 12, 24, 8, 2.5),
    Tablet("Huawei MatePad Pro", 599, 13, 12, 10.8, 14),
    Smartphone("Oppo Find X3", 799, 16, 12, 6.7, 24),
    Laptop("Razer Blade 15", 1599, 4, 24, 16, 3.5)
]

user1 = Cart()

while True:
    print("\nMenu:")
    print("1. Show Devices")
    print("2. Show Cart")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        for idx, device in enumerate(devices):
            print(f"{idx + 1}. {device.display_info()}")
        device_choice = int(input("Enter the number of the device to add to cart: ")) - 1
        if 0 <= device_choice < len(devices):
            amount = int(input("Enter the quantity: "))
            if devices[device_choice].is_available(amount):
                user1.add_device(devices[device_choice], amount)
                devices[device_choice].reduce_stock(amount)
                print(f"Added {amount} {devices[device_choice].name} to cart.")
            else:
                print("Not enough stock available.")
        else:
            print("Invalid choice.")
    elif choice == '2':
        print(user1.items)
        if not user1.items:
            print("Your cart is empty.")
        else:
            for item in user1.items:
                print(f"{item['device'].name} - Quantity: {item['amount']}, Total Price: {item['device'].price * item['amount']}")
            print(f"Total Cart Price: {user1.get_total_price()}")
    elif choice == '3':
        print(user1.checkout())
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
