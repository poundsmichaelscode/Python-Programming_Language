

#set are unordered collections of unique items
# sets are mutable meaning you can add or remove items after the set has been created i.e you can modify the set
# sets are defined using curly braces {} or the set() function  

# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}


my_set.add(6)  # Adding an item to the set
my_set.add(9)

print(my_set)  # Output: {1, 2, 3, 4, 5, 6, 9}


print(f"Number of Set is: {len(my_set)}")  # Output: 7