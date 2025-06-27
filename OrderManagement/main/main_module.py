import sys
import os
from typing import List

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from dao.order_processor import OrderProcessor
from entity.user import User
from entity.product import Product
from entity.electronics import Electronics
from entity.clothing import Clothing

def create_user_input():
    user_id = int(input("Enter User ID: "))
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    role = input("Enter Role (Admin/User): ")
    return User(user_id, username, password, role)

def create_product_input():
    product_id = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    desc = input("Enter Description: ")
    price = float(input("Enter Price: "))
    stock = int(input("Enter Quantity in Stock: "))
    type_ = input("Enter Product Type (Electronics/Clothing): ")

    if type_.lower() == "electronics":
        brand = input("Enter Brand: ")
        warranty = int(input("Enter Warranty Period (in months): "))
        return Electronics(product_id, name, desc, price, stock, type_, brand, warranty)
    elif type_.lower() == "clothing":
        size = input("Enter Size: ")
        color = input("Enter Color: ")
        return Clothing(product_id, name, desc, price, stock, type_, size, color)
    else:
        print("Invalid product type.")
        return None

def create_order_input():
    product_ids = input("Enter Product IDs (comma-separated): ").split(',')
    products = []
    for pid in product_ids:
        prod = Product(int(pid), "", "", 0, 0, "")
        products.append(prod)
    return products

if __name__ == "__main__":
    processor = OrderProcessor()

    while True:
        print("\n--- Order Management Menu ---")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Order by User")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            user = create_user_input()
            processor.create_user(user)

        elif choice == "2":
            user = create_user_input()
            product = create_product_input()
            if product:
                processor.create_product(user, product)

        elif choice == "3":
            user = create_user_input()
            products = create_order_input()
            processor.create_order(user, products)

        elif choice == "4":
            uid = int(input("Enter User ID: "))
            oid = int(input("Enter Order ID: "))
            processor.cancel_order(uid, oid)

        elif choice == "5":
            processor.get_all_products()

        elif choice == "6":
            uid = int(input("Enter User ID: "))
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            role = input("Enter Role: ")
            user = User(uid, username, password, role)
            processor.get_order_by_user(user)

        elif choice == "7":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid choice. Please try again.")
