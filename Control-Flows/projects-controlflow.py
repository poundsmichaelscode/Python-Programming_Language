# monthly_income = input("Enter your monthly income: ")
# monthly_income = float(monthly_income)

# monthly_expenses = input("Enter your monthly expenses: ")
# monthly_expenses = float(monthly_expenses)
# savings_rate = input("Enter your desired savings rate (as a percentage): ")
# savings_rate = float(savings_rate) / 100

# Projected_Savings = (monthly_income - monthly_expenses) * savings_rate * 12
# print(" Your Projected annual savings:", Projected_Savings)





print ("=====Personal Budget Summary===============")

#Step 1
name = input("What is your name? ")


#step 2

valid =False
while not valid:


    monthly_income = float(input("What is your monthly income"))
    print("Monthly Income:", monthly_income)
if type(monthly_income) is not float:
    print   ("Please enter a valid number for income.")

else:
    valid = True
    print("please enter a valid number for income.")


valid =False
while not valid:
    rent = (input("What is your monthly rent/mortgage payment"))
    print("Monthly Rent/Mortgage Payment:",)
    if rent.replace('.','',1).isdigit():  #check if input is a valid number a digit
        rent = float(rent)  #convert to float
        valid = True

    else:
            valid = True
            print("please enter a valid number for rent/mortgage payment.")




valid =False
while not valid:
    groceries = (input("What is your monthly groceries expense"))

print("Monthly Groceries Expense:",)
if groceries.replace('.','',1).isdigit():  #check if input is a valid number a digit
        groceries = float(groceries)  #convert to float 

        valid = True
else:
            valid = True
            print("please enter a valid number for groceries expense.")



valid =False
while not valid:

 transportation =(input("What is your monthly transportation expense"))   
print("Monthly Transportation Expense:",)
if transportation.replace('.','',1).isdigit():  #check if input is a valid number a digit
        transportation = float(transportation)  #convert to float
        valid = True
else:
            valid = True
            print("please enter a valid number for transportation expense.")    

valid =False    
while not valid: 

    entertainment = (input("What is your monthly entertainment expense"))  

print("Monthly Entertainment Expense:",)
if entertainment.replace('.','',1).isdigit():  #check if input is a valid number a digit
        entertainment = float(entertainment)  #convert to float 
        valid = True
else:
            valid = True
            print("please enter a valid number for entertainment expense.")


    #Step 3


total_expenses = rent + groceries + transportation + entertainment

remaining_balance = monthly_income - total_expenses

if  total_expenses > 0:
      savings_ratio = (remaining_balance / monthly_income) * 100
else:
        savings_ratio = 0

#Step 4
print(f"=====Personal Budget Summary for {name}===============")

print("Name:", name)
print(f"Monthly Income:  ${monthly_income}") 
print(f"Total Monthly Expenses:, ${total_expenses}")
print(f"Remaining Balance:, ${remaining_balance}")
print(f"Savings Ratio:   {savings_ratio:.2f}%")   


  #  # Step 5: Budget Evaluation
if savings_ratio >= 20:
    print(f"Great job!, your saving ratio is {savings_ratio} You are saving a good portion of your income.")

elif savings_ratio >= 10:
    
    print(f"Good effort! your saving ratio is {savings_ratio} Consider finding ways to save more.")

else:
    print(f"your saving ratio is {savings_ratio} !!! You might want to review your expenses and find areas to cut back.")  


#step 6 

choice = input("Would you like to see a breakdown of your expenses? (yes/no): ")
if choice.lower() == "yes":
    print("Expense Breakdown:")
    print(f"Rent/Mortgage: ${rent}")
    print(f"Groceries: ${groceries}")
    print(f"Transportation: ${transportation}")
    print(f"Entertainment: ${entertainment}")

#  # Conclusion
print("Thank you for using the Personal Budget Calculator. Stay financially healthy!")