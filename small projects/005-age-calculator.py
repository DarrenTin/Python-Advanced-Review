from datetime import datetime

current_date = datetime.now()
# birthdate = "2004-07-16"
birthdate = input("birthdate (yyyy-mm-dd): ")

birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
age = current_date - birthdate
remaining_life = 30000 - age.days
life_progress = f"{age.days / 30000 * 100:.2f}"

age = f"{age.days / 365.25:.2f}"
remaining_life = f"{remaining_life / 365.25:.2f}"

def visualized_bar(went):
    went = float(went) // 10
    to_go = 8 - went  # assume 80 years of lifespan
    bar = f"{'✅' * int(went)}{'❌' * int(to_go)}"
    return bar

print(age + " years old.")
print(remaining_life + " years to die.")
print(life_progress + r"% of your life has passed.")
print(f"progress => {visualized_bar(age)}")