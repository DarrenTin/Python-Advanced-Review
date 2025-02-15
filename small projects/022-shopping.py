class ShoppingCart:
    def __init__(self):
        self.items = []
        self.no = 1

    def add_item(self, name, price, quantity):
        self.items.append([self.no, name, price, quantity])
        self.no += 1

    def display_cart(self):
        print('no\tname\t\tprice\tqty\ttotal')
        for item in self.items:
            total = item[2] * item[3]
            print(f'{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\t{total}')

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[2] * item[3]
        return total
    
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item('curry pack', 12.5, 3)
    cart.add_item('golden chicken', 25.5, 2)
    cart.display_cart()
    
    total = cart.calculate_total()
    print('total =', total)