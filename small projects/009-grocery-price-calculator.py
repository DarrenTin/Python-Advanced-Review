import json
import time

def is_duplicate(item, cart):
    with open(cart, 'r') as file:
        old_data = json.load(file)
        for i in old_data:
            if i['item'] == item:
                return True
        return False

def add_item(item, price, cart):
    if is_duplicate(item, cart):
        print('cannot add duplicated item')
        return
    new_data = {'item': item, 'price': price}
    with open(cart, 'r+') as file:
        old_data = json.load(file)
        old_data.append(new_data)
        file.seek(0)
        json.dump(old_data, file, indent=4)
        print(f'item added: {new_data}')

def compute_total(cart):
    with open(cart, 'r') as file:
        old_data = json.load(file)
        total = sum(i['price'] for i in old_data)
        return total
    
def update_item(item, new_price, cart):
    with open(cart, 'r+') as file:
        old_data = json.load(file)
        for i in old_data:
            if i['item'] == item:
                i['price'] = new_price
        file.seek(0)
        json.dump(old_data, file, indent=4)
        print(f"price of {item} updated to {new_price}")

def delete_item(item, cart):
    # password = input("type 'password' to delete: ")
    # if password == 'password':
    with open(cart, 'r+') as file:
        old_data = json.load(file)
        old_data = [i for i in old_data if i['item'] != item]  # delete
        file.seek(0)
        file.truncate()
        json.dump(old_data, file, indent=4)
        print(f"item {item} is deleted")

def clear_cart(cart):
        with open(cart, 'r+') as file:
            file.truncate()
        print("cart is cleared")

cart = "009-grocery.json"

while True:
    print("1 - add\n2 - total\n3 - update\n4 - delete\n5 - clear\n6 - exit")
    option = input("option: ")
    if option == '1':
        item_name = input('item name: ')
        price = float(input('price: '))
        add_item(item_name, price, cart)
    elif option == '2':
        print('\n[receipt]')
        print('--------------------------')
        with open(cart, 'r') as file:
            old_data = json.load(file)
            print("item\tprice")
            for i in old_data:
                print(f"{i['item']}\t{i['price']}")
        print('--------------------------')
        print("Total = ", compute_total(cart), '\n')
    elif option == '3':
        item_name = input('item to update: ')
        new_price = float(input('new price: '))
        update_item(item_name, new_price, cart)
    elif option == '4':
        item_name = input('item to delete: ')
        delete_item(item_name, cart)
    elif option == '5':
        clear_cart(cart)
    elif option == '6':
        print("thanks for shopping with us!")
    else:
        print('invalid option!')
    
    time.sleep(3)