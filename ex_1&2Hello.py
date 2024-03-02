from datetime import datetime

name = input("Enter your name: ")
age = input("Enter your age: ")
name_length = len(name)
current_year = datetime.now().year
years_to_18= 18 - int(age)

print("Hello!", name)
print("Your name has", name_length, "letters and it starts with", name[0])
print( "You are", age, "years old, next year you will be", int(age) + 1, "years old. Your date of birth is",  current_year - int(age))

amount_of_money = input("Enter the amount of money you have: ")
missing_money = 20 - int(amount_of_money)
if int(amount_of_money) >= 20 and int(age)> 18:
    print("You can buy alcohol")
elif int(amount_of_money) < 20 and int(age) > 18:
    print("You can't buy alcohol, you don't have enough money. You need", missing_money, "more")
elif int(amount_of_money) < 20 and int(age) < 18:
    print("You can't buy alcohol, you are too young and poor")
else: 
    print("You are too young to buy alcohol, come back In", years_to_18, "years")