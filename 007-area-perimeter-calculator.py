from math import pi as pi
from math import sqrt as sqrt
from math import tan as tan

available_shapes = ['square', 'rectangle', 'circle', 
                    'triangle', 'parallelogram', 'trapezoid', 
                    'ellipse', 'rhombus', 'regular polygon']

def print_available_shapes():
    print('available shapes\n-------------')
    for count, shape in enumerate(available_shapes):
        print(count + 1, '-', shape)
    print('-------------')

def check_if_shape_exist(shape_name):
    if shape_name.isdigit():
        try:
            available_shapes[int(shape_name) - 1]
            return True
        except IndexError:
            return False
    elif shape_name in available_shapes:
        return True
    else:
        return False

def get_formula(shape_name):
    if shape_name == 'square':
        return f'Area of {shape_name} = side², Perimeter = 4 × side'
    elif shape_name == 'rectangle':
        return f'Area of {shape_name} = length × width, Perimeter = 2 × (length + width)'
    elif shape_name == 'circle':
        return f'Area of {shape_name} = π × radius², Perimeter (Circumference) = 2 × π × radius'
    elif shape_name == 'triangle':
        return f'Area of {shape_name} = 0.5 × base × height, Perimeter = side1 + side2 + base'
    elif shape_name == 'parallelogram':
        return f'Area of {shape_name} = base × height, Perimeter = 2 × (base + side)'
    elif shape_name == 'trapezoid':
        return f'Area of {shape_name} = 0.5 × (a + b) × height, Perimeter = a + b + side1 + side2'
    elif shape_name == 'ellipse':
        return f'Area = π × major_axis × minor_axis, Perimeter (approx.) = π × (3 × (major_axis + minor_axis) - sqrt((3 × major_axis + minor_axis) × (major_axis + 3 × minor_axis)))'
    elif shape_name == 'rhombus':
        return f'Area of {shape_name} = 0.5 × diagonal1 × diagonal2, Perimeter = 4 × side'
    elif shape_name == 'regular polygon':
        return f'Area of {shape_name} = (num_sides × side²) / (4 × tan(π / num_sides)), Perimeter = num_sides × side'
    
def input_shape_info(shape_name):
    if shape_name == 'square':
        side = float(input('Enter the side length: '))
        return {'side': side}
    elif shape_name == 'rectangle':
        length = float(input('Enter the length: '))
        width = float(input('Enter the width: '))
        return {'length': length, 'width': width}
    elif shape_name == 'circle':
        radius = float(input('Enter the radius: '))
        return {'radius': radius}
    elif shape_name == 'triangle':
        base = float(input('Enter the base: '))
        height = float(input('Enter the height: '))
        side1 = float(input('Enter side 1: '))
        side2 = float(input('Enter side 2: '))
        return {'base': base, 'height': height, 'side1': side1, 'side2': side2}
    elif shape_name == 'parallelogram':
        base = float(input('Enter the base: '))
        height = float(input('Enter the height: '))
        side = float(input('Enter the side length: '))
        return {'base': base, 'height': height, 'side': side}
    elif shape_name == 'trapezoid':
        a = float(input('Enter the length of base 1: '))
        b = float(input('Enter the length of base 2: '))
        height = float(input('Enter the height: '))
        side1 = float(input('Enter side 1: '))
        side2 = float(input('Enter side 2: '))
        return {'a': a, 'b': b, 'height': height, 'side1': side1, 'side2': side2}
    elif shape_name == 'ellipse':
        major_axis = float(input('Enter the major axis length: '))
        minor_axis = float(input('Enter the minor axis length: '))
        return {'major_axis': major_axis, 'minor_axis': minor_axis}
    elif shape_name == 'rhombus':
        diagonal1 = float(input('Enter the first diagonal length: '))
        diagonal2 = float(input('Enter the second diagonal length: '))
        side = float(input('Enter the side length: '))
        return {'diagonal1': diagonal1, 'diagonal2': diagonal2, 'side': side}
    elif shape_name == 'regular polygon':
        side = float(input('Enter the side length: '))
        num_sides = int(input('Enter the number of sides: '))
        return {'side': side, 'num_sides': num_sides}
    
def calculate_area(shape_name, params):
    if shape_name == 'square':
        return params['side'] ** 2
    elif shape_name == 'rectangle':
        return params['length'] * params['width']
    elif shape_name == 'circle':
        return pi * params['radius'] ** 2
    elif shape_name == 'triangle':
        return 0.5 * params['base'] * params['height']
    elif shape_name == 'parallelogram':
        return params['base'] * params['height']
    elif shape_name == 'trapezoid':
        return 0.5 * (params['a'] + params['b']) * params['height']
    elif shape_name == 'ellipse':
        return pi * params['major_axis'] * params['minor_axis']
    elif shape_name == 'rhombus':
        return 0.5 * params['diagonal1'] * params['diagonal2']
    elif shape_name == 'regular polygon':
        return (params['num_sides'] * params['side'] ** 2) / (4 * tan(pi / params['num_sides']))

def calculate_perimeter(shape_name, params):
    if shape_name == 'square':
        return 4 * params['side']
    elif shape_name == 'rectangle':
        return 2 * (params['length'] + params['width'])
    elif shape_name == 'circle':
        return 2 * pi * params['radius']
    elif shape_name == 'triangle':
        return params['side1'] + params['side2'] + params['base']
    elif shape_name == 'parallelogram':
        return 2 * (params['base'] + params['side'])
    elif shape_name == 'trapezoid':
        return params['a'] + params['b'] + params['side1'] + params['side2']
    elif shape_name == 'ellipse':
        return pi * (3 * (params['major_axis'] + params['minor_axis']) - 
                          sqrt((3 * params['major_axis'] + params['minor_axis']) * 
                                    (params['major_axis'] + 3 * params['minor_axis'])))
    elif shape_name == 'rhombus':
        return 4 * params['side']
    elif shape_name == 'regular polygon':
        return params['num_sides'] * params['side']

def app():
    print('welcome to area perimeter calculator')
    print('---------------------------------------')
    print('1. print supported shape')
    print('2. choose your shape')
    print('3. check formula of shape')
    print('4. get perimeter')
    print('5. get area')
    print('6. exit')

    chosen_shape = None

    while True:
        option = int(input('option: '))

        if option == 1:
            print_available_shapes()
        elif option == 2:
            chosen_shape = input('shape: ')
            exist = check_if_shape_exist(chosen_shape)
            if not exist:
                print(f'shape {chosen_shape} not exist!')
            else:
                if chosen_shape.isdigit():
                    try:
                        chosen_shape = available_shapes[int(chosen_shape) - 1]
                        print(f'you choose: {chosen_shape}')
                    except IndexError:
                        print(f'shape {int(chosen_shape)} not exist')
        elif option == 3:
            exist = check_if_shape_exist(chosen_shape)
            if not exist:
                print(f'please choose your shape first')
            else:
                formula = get_formula(chosen_shape)
                print(formula)
        elif option == 4:
            if not chosen_shape:
                print("please choose your shape first")
                continue
            shape_data = input_shape_info(chosen_shape)
            perimeter = calculate_perimeter(shape_name=chosen_shape, params=shape_data)
            print(f'perimeter: {perimeter:.2f}')
        elif option == 5:
            if not chosen_shape:
                print("please choose your shape first")
                continue
            shape_data = input_shape_info(chosen_shape)
            area = calculate_area(shape_name=chosen_shape, params=shape_data)
            print(f'area: {area:.2f}')
        elif option == 6:
            break

app()