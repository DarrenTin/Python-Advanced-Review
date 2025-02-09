class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_item(self, name, price, quantity):
        """Adds an item to the cart with name, price, and quantity."""
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive numbers.")
            return
        self.cart.append({"name": name, "price": price, "quantity": quantity})
        print(f"Added {quantity} x {name} @ ${price:.2f} each.")

    def display_cart(self):
        """Displays the shopping cart items."""
        if not self.cart:
            print("\nYour cart is empty.")
            return
        print("\n🛒 Shopping Cart:")
        for index, item in enumerate(self.cart, 1):
            total_price = item["price"] * item["quantity"]
            print(f"{index}. {item['name']} - ${item['price']:.2f} x {item['quantity']} = ${total_price:.2f}")
        total_price = sum(item["price"] * item["quantity"] for item in self.cart)
        print(f"\nTotal: ${total_price:.2f}")

    def calculate_total(self, discount_type=None, discount_value=0):
        """Calculates the total bill after applying discounts."""
        subtotal = sum(item["price"] * item["quantity"] for item in self.cart)
        
        discount = 0
        if discount_type == "percentage":
            discount = (discount_value / 100) * subtotal
        elif discount_type == "fixed":
            discount = discount_value

        discount = min(discount, subtotal)  # Ensure discount is not greater than subtotal
        total = subtotal - discount
        
        print("\n💰 Bill Summary:")
        print(f"Subtotal: ${subtotal:.2f}")
        if discount > 0:
            discount_text = f"{discount_value}% off" if discount_type == "percentage" else f"${discount_value} off"
            print(f"Discount Applied ({discount_text}): -${discount:.2f}")
        print(f"Total Amount: ${total:.2f}")
        return total

# Main Program
if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Apply Discount & Checkout")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter item name: ").strip()
            try:
                price = float(input("Enter item price: "))
                quantity = int(input("Enter item quantity: "))
                cart.add_item(name, price, quantity)
            except ValueError:
                print("Invalid input! Price must be a number and quantity must be an integer.")

        elif choice == "2":
            cart.display_cart()

        elif choice == "3":
            cart.display_cart()
            discount_type = input("Apply discount? (percentage/fixed/none): ").strip().lower()
            discount_value = 0
            if discount_type in ["percentage", "fixed"]:
                try:
                    discount_value = float(input("Enter discount value: "))
                    if discount_value < 0:
                        print("Discount cannot be negative!")
                        continue
                except ValueError:
                    print("Invalid discount value! Must be a number.")
                    continue
            cart.calculate_total(discount_type, discount_value)

        elif choice == "4":
            print("Thank you for shopping with us! 🛍️")
            break

        else:
            print("Invalid option! Please choose a valid number.")
