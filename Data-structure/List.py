# Sequence of mutable values in python a list is defined using square brackets []
# Lists can store multiple items in a single variable
# a list is mutable meaning you can change, add, remove items after the list has been created i.e you can modify the list
# Lists can contain items of different data types including numbers, strings, and even other lists 
# Creating a list
# Alist can be changed after its creation


fruits = ["apple", "banana", "cherry", "date", "elderberry","fig", "grape"]

print(fruits)  # Output: ['apple', 'banana', 'cherry'............]

print([2])

fruits.append("honeydew")  # Adding an item to the end of the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', .........., 'honeydew']

fruits.remove("date")  # Removing an item from the list
print(fruits)  # Output: ['apple', 'banana', 'cherry', .........., 'honeydew']        


fruits.sort()  # Sorting the list in ascending order

print(fruits)  # Output: ['apple', 'banana', 'cherry', .........., 'honeydew']