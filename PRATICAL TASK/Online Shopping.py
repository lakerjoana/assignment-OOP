class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")

class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
        else:
            print("Insufficient quantity in stock")

    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]
                break

    def display_cart(self):
        for item in self.items:
            print(f"Product Name: {item[0].product_name}")
            print(f"Quantity: {item[1]}")
            print(f"Price: {item[0].price * item[1]}")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[0].price * item[1]
        return total

# Create three Product objects
product1 = Product("Product A", 100, 10)
product2 = Product("Product B", 200, 5)
product3 = Product("Product C", 300, 8)

# Create two ShoppingCart instances
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Add products to cart
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)
cart2.add_to_cart(product3, 3)

# Display cart contents
cart1.display_cart()
cart2.display_cart()

# Calculate total
print(f"Total for Cart 1: {cart1.calculate_total()}")
print(f"Total for Cart 2: {cart2.calculate_total()}")