def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = 100
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} celsius is equal to {fahrenheit:.2f} fahrenheit")

fahrenheit = 100
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit} fahrenheit is equal to {celsius:.2f} celsius")