

moneyEarned = float(input("Please enter the amount of money you make a month: "))
tithing = moneyEarned * 0.10
offering = float(input("How much would you like to offer for fast and offerings?: "))



item1 = input("Please enter your item: ")
amount1 = int(input("Please enter your amount: "))
item2 = input("Please enter your item: ")
amount2 = int(input("Please enter your amount: "))
item3 = input("Please enter your item: ")
amount3 = int(input("Please enter your amount: "))
item4 = input("Please enter your item: ")
amount4 = int(input("Please enter your amount: "))
item5 = input("Please enter your item: ")
amount5 = int(input("Please enter your amount: "))
totalExpenses = amount1 + amount2 + amount3 + amount4 + amount5

savings = moneyEarned - totalExpenses


print("Personal budget")
print("=============================================")
print("Income    |Month      |Year")
print(f"           ${moneyEarned}      ${moneyEarned*12}")
print("Expenses  |Month      |Year")
print(f"Thiting    ${moneyEarned}      ${moneyEarned*12}")
print(f"{item1}       ${amount1}        ${amount1*12}")
print(f"{item2}       ${amount2}        ${amount2*12}")
print(f"{item3}       ${amount3}        ${amount3*12}")
print(f"{item4}       ${amount4}        ${amount4*12}")
print(f"{item5}       ${amount5}        ${amount5*12}")
print("=============================================")
print("Savings   |Month      |Year")
print(f"         ${savings} ${savings*12}")