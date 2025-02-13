def menu():
    print("1 - dec to bin/oct/hex")
    print("2 - bin/oct/hex to dec")
    option = input('option:')
    return option

def dec_to_base(dec):
    b = bin(dec)[2:]
    o = oct(dec)[2:]
    h = hex(dec)[2:]
    result = f'bin = {b}\toct = {o}\thex = {h}'
    return result

def base_to_dec(basenum, base):
    if base == 2:
        result = int(basenum, 2)
    elif base == 8:
        result = int(basenum, 8)
    elif base == 16:
        result = int(basenum, 16)
    else:
        return "base not supported"
    return result

def convertor():
    option = menu()

    try:
        if option == '1':
            dec = int(input('dec num:'))
            print(dec_to_base(dec))
        elif option == '2':
            basenum = input('base num:')
            base = int(input('base:'))
            print(base_to_dec(basenum, base))
        else:
            print('option not supported')
    except ValueError as e:
        if "Exceeds the limit" in str(e):
            print('number too large')
        elif "invalid literal" in str(e):
            print('data type error')
        else:
            print(e)

convertor()