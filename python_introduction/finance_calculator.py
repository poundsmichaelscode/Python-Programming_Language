monthly_income = input("Enter your monthly income: ")
monthly_income = float(monthly_income)

monthly_expenses = input("Enter your monthly expenses: ")
monthly_expenses = float(monthly_expenses)
savings_rate = input("Enter your desired savings rate (as a percentage): ")
savings_rate = float(savings_rate) / 100

Projected_Savings = (monthly_income - monthly_expenses) * savings_rate * 12
print(" Your Projected annual savings:", Projected_Savings)



