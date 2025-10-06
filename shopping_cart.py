# shopping_cart.py
# Main menu-driven script to run the shopping cart app

from products import products
import cart_ops as ops

def menu():
    cart = []
    while True:
        print("===== Shopping Cart =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Update Cart")
        print("5. Remove from Cart")
        print("6. Checkout")
        print("7. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input — please enter a number between 1 and 7.\n")
            continue

        if choice == 1:
            ops.view_products(products)

        elif choice == 2:
            try:
                pid = int(input("Enter Product ID to add: "))
                qty = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input — IDs and quantities must be integers.\n")
                continue
            ok, msg = ops.add_to_cart(products, cart, pid, qty)
            print(msg + "\n")

        elif choice == 3:
            ops.view_cart(cart)

        elif choice == 4:
            try:
                pid = int(input("Enter Product ID to update: "))
                qty = int(input("Enter new quantity: "))
            except ValueError:
                print("Invalid input — IDs and quantities must be integers.\n")
                continue
            ok, msg = ops.update_cart(cart, pid, qty)
            print(msg + "\n")

        elif choice == 5:
            try:
                pid = int(input("Enter Product ID to remove: "))
            except ValueError:
                print("Invalid input — IDs must be integers.\n")
                continue
            ok, msg = ops.remove_from_cart(cart, pid)
            print(msg + "\n")

        elif choice == 6:
            ok, bill_or_msg = ops.checkout(cart)
            if ok:
                print(bill_or_msg)
            else:
                print(bill_or_msg + "\n")

        elif choice == 7:
            print("Exiting — goodbye!")
            break

        else:
            print("Please choose a number between 1 and 7.\n")

if __name__ == '__main__':
    menu()
