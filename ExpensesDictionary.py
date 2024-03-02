expenses = {
    "january": "1500",
    "february": "2200",
    "march": "2000",
    "april": "2500",
    "may": "2000",
    "june": "1800",
    "july": "1900",
    "august": "2000",
    "september": "2200",
    "october": "2000",
    "november": "1500",
    "december": "2500"
}
print("Minimum expense is", min(expenses, key=expenses.get))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Maximum expense is", max(expenses, key=expenses.get))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total expense is", sum(int(i) for i in expenses.values()))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Average expense is", sum(int(i) for i in expenses.values())/len(expenses))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for month, expense in expenses.items():
    if int(expense) > sum(int(i) for i in expenses.values()) / len(expenses):
        print(f"Expense in {month} is greater than the average expense. You should spent less.")
    else:
        print(f"Expense in {month} is not greater than the average expense. Nice")