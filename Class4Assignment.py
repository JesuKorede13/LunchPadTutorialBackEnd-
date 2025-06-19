"""

1. Why use tuples instead of lists?

2. Define a tuple of names that is ten items in length.

3. Try to modify the seventh item in the tuple. What happens? Record your observations.

4. Write a for loop to print out each item in the tuple with their indexes. 

Answers 

1. Why use tuples instead of lists?*

Tuples are immutable, meaning their contents cannot be modified after creation. This provides benefits like:
- Code safety
- Performance optimization
- Hashability (tuples can be used as dictionary keys)

Use tuples when data shouldn't change.

2. Define a tuple of names that is ten items in length.

"""
names_tuple = ("John", "Alice", "Bob", "Eve", "Mike", "Emma", "Tom", "Lily", "Sam", "Sophia")

# 3. Try to modify the seventh item in the tuple. What happens?
"""
names_tuple[6] = "Jerry"

This raises a `TypeError: 'tuple' object does not support item assignment`.
Tuples are immutable, so you can't modify their elements directly.

"""

# 4. Write a for loop to print out each item in the tuple with their indexes.
for index, name in enumerate(names_tuple, 1):
# the ",1" indicates that the index should start from 1 instead of 0
    print(f"Index: {index}, Name: {name}")
# This will output:
"""
Index: 1, Name: John
Index: 2, Name: Alice
Index: 3, Name: Bob
Index: 4, Name: Eve
Index: 5, Name: Mike
Index: 6, Name: Emma
Index: 8, Name: Tom
Index: 8, Name: Lily
Index: 9, Name: Sam
Index: 10, Name: Sophia
"""
