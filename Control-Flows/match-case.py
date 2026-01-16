# Basic Syntax:
# The basic syntax of a Match Case statement follows this structure:

# match expression:
#     case pattern1:
#         code_block_1
#     case pattern2:
#         code_block_2
#     ...
#     case pattern_n:
#         code_block_n
#     # Optional: _ (wildcard) for default case
# expression: This is the value you want to match against different patterns.
# case pattern: Each case statement defines a pattern to match against the expression.
# code_block: The code block associated with a matching pattern is indented and executed.
# _ (wildcard): An optional _(underscore) can be used as a wildcard pattern to match anything not explicitly covered by other cases. This serves as a default case. ### Matching Specific Values:
# Let’s see how Match Case simplifies checking for specific values:

# day = input("Enter a day of the week (Monday-Sunday): ").lower()

# match day:
#     case "monday":
#         print("Ugh, Mondays...")
#     case "tuesday":
#         print("Just another workday...")
#     case "wednesday":
#         print("Hump day!")
#     case "thursday":
#         print("Almost there...")
#     case "friday":
#         print("TGIF!")
#     case "saturday" | "sunday":  # Match multiple values with pipe (|)
#         print("Weekend vibes!")
#     case _:
#         print("Invalid day entered.")
# In this example, the day variable is matched against specific weekdays. Each matching case executes its corresponding code block, printing a message based on the user’s input. Notice how the | (pipe) operator allows matching against multiple values in a single case.

# Matching Data Types:
# Match Case can also be used to match against data types:

# value = input("Enter a value (number or string): ")

# match value:
#     case int():
#         print("You entered an integer:", value)
#     case str():
#         print("You entered a string:", value)
#     case _:
#         print("Invalid data type entered.")
# Here, the value variable is matched against data types. The int() and str() functions act as patterns, checking if the value is an integer or a string.

# These are just a few basic examples to demonstrate the core functionality of Match Case statements. As you progress, you’ll encounter more complex scenarios where Match Case can be a powerful tool for handling intricate conditions and data types effectively.

# Best Practices for Using Match Case Statements for Readability and Efficiency
# Match Case statements offer a clear and concise way to handle multiple conditions. However, just like any other tool, using them effectively involves following some best practices:

# Clarity over Conciseness: While Match Case promotes conciseness, prioritize clarity. If a complex case becomes hard to read, consider breaking it down into simpler cases for better understanding.
# Default Case (_): Include a default case using_ to catch any unmatched patterns. This prevents potential runtime errors if the expression doesn’t match any specific case.
# Complex Logic with Guards: For intricate logic within a case, consider using guards within the case statement itself. Guards are additional conditions that must be True for the case’s code block to execute. This can improve readability by separating the matching pattern from the specific logic within the case.
# Here’s an example demonstrating a guard within a case:

# age = int(input("Enter your age: "))

# match age:
#     case 18 | 19:  # Match multiple values with pipe (|)
#         if age >= 18 and has_id(user):  # Guard using a function call
#             print("You are eligible to vote.")
#         else:
#             print("You need a valid ID to vote.")
#     case _:
#         print("You are not yet eligible to vote.")
# In this example, the has_id function is used as a guard within the case for 18-19 year olds. This clarifies the specific condition for voting eligibility beyond just age.

# By following these practices, you can leverage Match Case statements to write clean, readable, and efficient code for handling complex control flow scenarios in your Python programs. Remember, Match Case is a powerful tool, but use it thoughtfully to enhance the clarity and maintainability of your code.




import random

random.randint(1, 10) ="secret_number"

users = input()
users = int(input("Guess the number"))