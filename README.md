# Shopping Cart Project (Python)

A simple console-based Shopping Cart application implemented in Python.

## Features
- View predefined products
- Add products to cart (max 8 distinct items)
- View cart with item subtotals and total bill
- Update item quantity in cart
- Remove items from cart
- Checkout (shows bill and empties cart)

## Requirements
- Python 3.8+

## Files
- `products.py` — Predefined list of products.
- `cart_ops.py` — Cart operation functions (add, view, update, remove, checkout).
- `shopping_cart.py` — Main menu script to run the app.

## How to run
1. Open a terminal.
2. Navigate to the project folder.
3. Run: `python shopping_cart.py`

## Notes
- The cart stores up to 8 distinct items. Adding quantity to an existing item does not increase the distinct item count.
- Prices are integers (INR) in this demo.

## License
MIT
