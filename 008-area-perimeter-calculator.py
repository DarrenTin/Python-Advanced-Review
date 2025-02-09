import math

# Function to calculate area and perimeter of different shapes
def calculate_area_and_perimeter(shape, **params):
    if shape == 'rectangle':
        length = params.get('length')
        width = params.get('width')
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter
    
    elif shape == 'circle':
        radius = params.get('radius')
        area = math.pi * (radius ** 2)
        perimeter = 2 * math.pi * radius
        return area, perimeter
    
    elif shape == 'triangle':
        base = params.get('base')
        height = params.get('height')
        side1 = params.get('side1')
        side2 = params.get('side2')
        area = 0.5 * base * height
        perimeter = side1 + side2 + base
        return area, perimeter
    
    elif shape == 'square':
        side = params.get('side')
        area = side ** 2
        perimeter = 4 * side
        return area, perimeter
    
    elif shape == 'parallelogram':
        base = params.get('base')
        height = params.get('height')
        side = params.get('side')
        area = base * height
        perimeter = 2 * (base + side)
        return area, perimeter
    
    elif shape == 'trapezoid':
        a = params.get('a')  # length of one base
        b = params.get('b')  # length of other base
        height = params.get('height')
        side1 = params.get('side1')
        side2 = params.get('side2')
        area = 0.5 * (a + b) * height
        perimeter = a + b + side1 + side2
        return area, perimeter
    
    elif shape == 'ellipse':
        major_axis = params.get('major_axis')
        minor_axis = params.get('minor_axis')
        area = math.pi * major_axis * minor_axis
        # Perimeter approximation (Ramanujan's formula)
        perimeter = math.pi * (3 * (major_axis + minor_axis) - math.sqrt((3 * major_axis + minor_axis) * (major_axis + 3 * minor_axis)))
        return area, perimeter
    
    elif shape == 'rhombus':
        diagonal1 = params.get('diagonal1')
        diagonal2 = params.get('diagonal2')
        side = params.get('side')
        area = 0.5 * diagonal1 * diagonal2
        perimeter = 4 * side
        return area, perimeter
    
    elif shape == 'regular_polygon':
        side = params.get('side')
        num_sides = params.get('num_sides')
        # Area of regular polygon
        area = (num_sides * side**2) / (4 * math.tan(math.pi / num_sides))
        # Perimeter of regular polygon
        perimeter = num_sides * side
        return area, perimeter
    
    else:
        return "Shape not recognized."

# Example usage
shape = input("Enter the shape (rectangle, circle, triangle, square, parallelogram, trapezoid, ellipse, rhombus, regular_polygon): ").lower()

if shape == 'rectangle':
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area, perimeter = calculate_area_and_perimeter(shape, length=length, width=width)

elif shape == 'circle':
    radius = float(input("Enter the radius: "))
    area, perimeter = calculate_area_and_perimeter(shape, radius=radius)

elif shape == 'triangle':
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    area, perimeter = calculate_area_and_perimeter(shape, base=base, height=height, side1=side1, side2=side2)

elif shape == 'square':
    side = float(input("Enter the side: "))
    area, perimeter = calculate_area_and_perimeter(shape, side=side)

elif shape == 'parallelogram':
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    side = float(input("Enter the side: "))
    area, perimeter = calculate_area_and_perimeter(shape, base=base, height=height, side=side)

elif shape == 'trapezoid':
    a = float(input("Enter the length of base 1: "))
    b = float(input("Enter the length of base 2: "))
    height = float(input("Enter the height: "))
    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    area, perimeter = calculate_area_and_perimeter(shape, a=a, b=b, height=height, side1=side1, side2=side2)

elif shape == 'ellipse':
    major_axis = float(input("Enter the length of the major axis: "))
    minor_axis = float(input("Enter the length of the minor axis: "))
    area, perimeter = calculate_area_and_perimeter(shape, major_axis=major_axis, minor_axis=minor_axis)

elif shape == 'rhombus':
    diagonal1 = float(input("Enter the length of the first diagonal: "))
    diagonal2 = float(input("Enter the length of the second diagonal: "))
    side = float(input("Enter the length of the side: "))
    area, perimeter = calculate_area_and_perimeter(shape, diagonal1=diagonal1, diagonal2=diagonal2, side=side)

elif shape == 'regular_polygon':
    side = float(input("Enter the length of one side: "))
    num_sides = int(input("Enter the number of sides: "))
    area, perimeter = calculate_area_and_perimeter(shape, side=side, num_sides=num_sides)

else:
    area, perimeter = "Shape not recognized.", ""

# Output the results
if isinstance(area, (int, float)) and isinstance(perimeter, (int, float)):
    print(f"Area: {area:.2f}")
    print(f"Perimeter: {perimeter:.2f}")
else:
    print(area)
