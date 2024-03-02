print("Hello there! I am a tax calculator. I will help you calculate your taxes.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("I will ask you a few questions and then I will calculate your taxes.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Tell me If you want to pass in monthly or yearly income")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

income_type = input("Enter M for monthly or Y for yearly: ")
if income_type == "M":
    monthly_income = input("Enter your monthly income: ")
    yearly_income = int(monthly_income) * 12
    print("Your yearly income is", yearly_income)
elif income_type == "Y":
    yearly_income = input("Enter your yearly income: ")

if int(yearly_income) <=120000:
    tax = int(yearly_income) *0.12
else :
    tax = int(yearly_income) *0.12 + (int(yearly_income) - 120000) * 0.32

print("Your tax is", tax)