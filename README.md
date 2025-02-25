# Electronic Device Shopping Cart

This project implements an electronic device shopping cart system using Object-Oriented Programming (OOP). Customers can browse, add devices to their cart, and purchase electronic devices such as smartphones, laptops, and tablets. The system manages stock levels and applies discounts.

The store offers different types of devices: Smartphones, Laptops, and Tablets.

Each device has common attributes like name, price, and stock, along with unique attributes for each device type.

Customers can:

**Add devices to their shopping cart.

Specify quantities.

Proceed to checkout.

Device Types & Attributes**

### 1. Smartphone

Attributes:

Screen size 

Battery life 

Methods:

make_call(): Simulates making a call.

install_app(): Simulates installing an app.

### 2. Laptop

Attributes:

RAM size (in GB)

Processor speed (in GHz)

Methods:

run_program(): Simulates running a program.

use_keyboard(): Simulates typing on the keyboard.

### 3. Tablet

Attributes:

Screen resolution

Weight (in grams)

Methods:

browse_internet(): Simulates browsing the internet.

use_touchscreen(): Simulates touchscreen navigation.

Class Structure

### 1. Device (Base Class)

Attributes:

name: Device name

price: Device price

stock: Available stock

warranty_period: Warranty period (months)

Methods:

display_info(): Displays device details.

apply_discount(discount_percentage): Reduces price by discount percentage.

is_available(amount): Checks if required quantity is available.

reduce_stock(amount): Deducts purchased quantity from stock.

### 2. Cart Class

Attributes:

items: List of tuples containing devices and quantities.

total_price: Total cart price.

Methods:

add_device(device, amount): Adds a device to the cart.

remove_device(device, amount): Removes a device from the cart.

get_total_price(): Retrieves total price.

print_items(): Displays items in the cart.

checkout(): Processes the purchase.

Running the Application

Steps:

Use the Menu: Interact with the menu-driven interface:

Option 1: Show Devices (Lists all available devices)

Option 2: Show Cart (Displays items in cart)

Option 3: Exit

Sample Input/Output
Menu:
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 

**Example 1: Displaying Devices**

Input: 1
1. Device name: iPhone 13, Price: 999, Stock: 10, Warranty period: 12
2. Device name: Samsung Galaxy S21, Price: 799, Stock: 15, Warranty period: 12
3. Device name: MacBook Pro, Price: 1299, Stock: 5, Warranty period: 24
4. Device name: Dell XPS 13, Price: 999, Stock: 8, Warranty period: 24
5. Device name: iPad Pro, Price: 799, Stock: 12, Warranty period: 12
6. Device name: Samsung Galaxy Tab S7, Price: 649, Stock: 10, Warranty period: 12
7. Device name: Google Pixel 6, Price: 599, Stock: 20, Warranty period: 12
8. Device name: HP Spectre x360, Price: 1099, Stock: 7, Warranty period: 24
9. Device name: Microsoft Surface Pro 7, Price: 749, Stock: 9, Warranty period: 12
10. Device name: OnePlus 9, Price: 729, Stock: 18, Warranty period: 12
11. Device name: Lenovo ThinkPad X1, Price: 1199, Stock: 6, Warranty period: 24
12. Device name: Amazon Fire HD 10, Price: 149, Stock: 25, Warranty period: 12
13. Device name: Sony Xperia 5 II, Price: 949, Stock: 11, Warranty period: 12
14. Device name: Asus ZenBook 14, Price: 899, Stock: 10, Warranty period: 24
15. Device name: Lenovo Tab P11 Pro, Price: 499, Stock: 14, Warranty period: 12
16. Device name: Xiaomi Mi 11, Price: 749, Stock: 17, Warranty period: 12
17. Device name: Acer Swift 3, Price: 699, Stock: 12, Warranty period: 24
18. Device name: Huawei MatePad Pro, Price: 599, Stock: 13, Warranty period: 12
19. Device name: Oppo Find X3, Price: 799, Stock: 16, Warranty period: 12
20. Device name: Razer Blade 15, Price: 1599, Stock: 4, Warranty period: 24
**Example 2: Adding a Device to Cart**
Enter the number of the device to add to cart: 20
Enter the quantity: 2
Added 2 Razer Blade 15 to cart.

**Example 3: Viewing Cart**
Input: 2
Razer Blade 15 - Quantity: 2, Total Price: 3198
Total Cart Price: 3198
**Example 4: Checkout**
Your total price is 3198. Thank you for shopping with us
Exiting the program.
## UML
[https://github.com/bbzet/Assignment5oop/blob/main/UMLassign5.png]



