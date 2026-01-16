


import sys
x = int (input("x:"))
y = int (input("y:"))
  
try:
result =x/y
except ZeroDivitionError:
    print("Error:Cannot Divide by 0.")

    sys.exit(1)
print (f"x / y {y} = {result}")



