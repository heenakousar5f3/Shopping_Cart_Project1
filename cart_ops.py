# cart_ops.py
# Functions to manage the shopping cart

MAX_CART_ITEMS = 8

def find_product(products, product_id):
    for p in products:
        if p['id'] == product_id:
            return p
    return None

def cart_size(cart):
    return len(cart)

def find_in_cart(cart, product_id):
    for item in cart:
        if item['id'] == product_id:
            return item
    return None

def view_products(products):
    print("\nAvailable Products:")
    print("ID\tName\t\tPrice")
    for p in products:
        print(f"{p['id']}\t{p['name']:<12}\t₹{p['price']}")
    print()

def add_to_cart(products, cart, product_id, quantity):
    if cart_size(cart) >= MAX_CART_ITEMS:
        return False, f"Cart can hold maximum {MAX_CART_ITEMS} distinct items."

    product = find_product(products, product_id)
    if not product:
        return False, "Product ID not found."

    if quantity <= 0:
        return False, "Quantity must be at least 1."

    existing = find_in_cart(cart, product_id)
    if existing:
        existing['quantity'] += quantity
    else:
        cart.append({
            'id': product['id'],
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity
        })
    return True, "Added to cart successfully."

def view_cart(cart):
    if not cart:
        print("\nYour cart is empty.\n")
        return

    print("\nYour Cart:")
    print("ID\tName\t\tPrice\tQty\tSubtotal")
    total = 0
    for item in cart:
        subtotal = item['price'] * item['quantity']
        total += subtotal
        print(f"{item['id']}\t{item['name']:<12}\t₹{item['price']}\t{item['quantity']}\t₹{subtotal}")
    print(f"\nTotal: ₹{total}\n")

def update_cart(cart, product_id, quantity):
    item = find_in_cart(cart, product_id)
    if not item:
        return False, "Item not found in cart."
    if quantity <= 0:
        return False, "Quantity must be at least 1."
    item['quantity'] = quantity
    return True, "Cart updated successfully."

def remove_from_cart(cart, product_id):
    item = find_in_cart(cart, product_id)
    if not item:
        return False, "Item not found in cart."
    cart.remove(item)
    return True, "Item removed from cart."

def checkout(cart):
    if not cart:
        return False, "Cart is empty."
    total = 0
    lines = []
    lines.append("\n----- BILL -----\n")
    lines.append("ID\tName\tQty\tPrice\tSubtotal\n")
    for item in cart:
        subtotal = item['price'] * item['quantity']
        total += subtotal
        lines.append(f"{item['id']}\t{item['name']}\t{item['quantity']}\t₹{item['price']}\t₹{subtotal}\n")
    lines.append(f"\nTOTAL: ₹{total}\n")
    lines.append("Thank you for shopping!\n")
    # empty the cart
    cart.clear()
    return True, ''.join(lines)
