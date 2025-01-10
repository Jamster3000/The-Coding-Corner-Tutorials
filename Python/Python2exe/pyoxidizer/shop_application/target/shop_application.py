import sys
import getpass
import json
from collections import defaultdict

# Data storage
USERS = {}
PRODUCTS = {
    "P001": {"name": "Laptop", "price": 1200},
    "P002": {"name": "Smartphone", "price": 800},
    "P003": {"name": "Headphones", "price": 100}
}
CARTS = defaultdict(list)
ORDERS = []

def load_data():
    global USERS, PRODUCTS, CARTS, ORDERS
    try:
        with open("users.json", "r") as f:
            USERS = json.load(f)
        with open("products.json", "r") as f:
            PRODUCTS = json.load(f)
        with open("carts.json", "r") as f:
            CARTS = json.load(f)
        with open("orders.json", "r") as f:
            ORDERS = json.load(f)
    except FileNotFoundError:
        pass

def save_data():
    with open("users.json", "w") as f:
        json.dump(USERS, f)
    with open("products.json", "w") as f:
        json.dump(PRODUCTS, f)
    with open("carts.json", "w") as f:
        json.dump(CARTS, f)
    with open("orders.json", "w") as f:
        json.dump(ORDERS, f)

def register():
    username = input("Enter username: ")
    if username in USERS:
        print("Username already exists.")
        return
    password = getpass.getpass("Enter password: ")
    USERS[username] = {"password": password}
    save_data()
    print("Registration successful.")

def login():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in USERS and USERS[username]["password"] == password:
        return username
    print("Invalid credentials.")
    return None

def browse_products():
    for code, product in PRODUCTS.items():
        print(f"{code}: {product['name']} - ${product['price']}")

def add_to_cart(username, product_code):
    if product_code in PRODUCTS:
        CARTS[username].append(product_code)
        save_data()
        print("Product added to cart.")
    else:
        print("Product not found.")

def view_cart(username):
    print(f"Cart for {username}:")
    for product_code in CARTS[username]:
        product = PRODUCTS[product_code]
        print(f"{product_code}: {product['name']} - ${product['price']}")

def checkout(username):
    total = 0
    order = []
    for product_code in CARTS[username]:
        product = PRODUCTS[product_code]
        total += product["price"]
        order.append((product_code, product["name"], product["price"]))
    CARTS[username] = []
    save_data()
    ORDERS.append((username, order, total))
    save_data()
    print(f"Checkout successful. Total: ${total}")

def view_order_history(username):
    print(f"Order history for {username}:")
    for idx, (order_username, order_products, total) in enumerate(ORDERS, start=1):
        if order_username == username:
            print(f"Order {idx}:")
            for product_code, product_name, product_price in order_products:
                print(f"- {product_name} - ${product_price}")
            print(f"Total: ${total}\n")

def main():
    load_data()
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Browse Products")
        print("4. Add to Cart")
        print("5. View Cart")
        print("6. Checkout")
        print("7. View Order History")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            username = login()
            if username:
                while True:
                    print("\nA. Browse Products")
                    print("B. Add to Cart")
                    print("C. View Cart")
                    print("D. Checkout")
                    print("E. View Order History")
                    print("F. Logout")
                    sub_choice = input("Enter sub-choice: ")

                    if sub_choice == "A":
                        browse_products()
                    elif sub_choice == "B":
                        product_code = input("Enter product code: ")
                        add_to_cart(username, product_code)
                    elif sub_choice == "C":
                        view_cart(username)
                    elif sub_choice == "D":
                        checkout(username)
                    elif sub_choice == "E":
                        view_order_history(username)
                    elif sub_choice == "F":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice.")
        elif choice == "3":
            browse_products()
        elif choice == "4":
            username = input("Enter your username: ")
            if username in USERS:
                product_code = input("Enter product code: ")
                add_to_cart(username, product_code)
            else:
                print("User not found.")
        elif choice == "5":
            username = input("Enter your username: ")
            if username in USERS:
                view_cart(username)
            else:
                print("User not found.")
        elif choice == "6":
            username = input("Enter your username: ")
            if username in USERS:
                checkout(username)
            else:
                print("User not found.")
        elif choice == "7":
            username = input("Enter your username: ")
            if username in USERS:
                view_order_history(username)
            else:
                print("User not found.")
        elif choice == "8":
            save_data()
            print("Exiting. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
