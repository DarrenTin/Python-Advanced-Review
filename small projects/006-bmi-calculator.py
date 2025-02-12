def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    bmi = round(bmi, 1)  # 1 decimal place
    return bmi

def group_bmi(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi >= 18.5 and bmi < 24.9:
        return 'normal weight'
    elif bmi >= 25 and bmi < 29.9:
        return 'overweight'
    else:
        return 'obesity'
    
test_data = {
    'Ali': {
        'weight': 45,
        'height': 1.3,
    },
    'Abu': {
        'weight': 55,
        'height': 1.2,
    },
    'Lily': {
        'weight': 35,
        'height': 1.4,
    },
}

print("test data\n-----------------------\nname\tweight\theight")
for person in test_data:
    weight = test_data[person]['weight']
    height = test_data[person]['height']
    print(f"{person}\t{weight}kg\t{height}m")

print("-----------------------")
for person in test_data:
    weight = test_data[person]['weight']
    height = test_data[person]['height']
    bmi = calculate_bmi(weight, height)
    group = group_bmi(bmi)
    print(f"name: {person}\nbmi: {bmi}\ngroup: {group}")
    print("-----")