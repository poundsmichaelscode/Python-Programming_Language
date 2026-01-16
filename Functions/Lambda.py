


people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25}, 
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28}
    
    ]



people.sort(key = lambda person: person["name"])

print(people)

