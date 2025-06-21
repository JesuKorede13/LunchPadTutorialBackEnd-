"""

Questions 
How can we use tuples as dictionary keys? 
Why is this possible and is it good practice?
Give an example.


Submission Format: Programiz link. Notes should be included as comments. Codes should run without errors.


Answers 

Using Tuples as Dictionary Keys
Tuples can be used as dictionary keys in Python because they are immutable, 
meaning their contents cannot be modified after creation. 
This immutability ensures that 
the tuple's hash value remains consistent, 
which is a requirement for dictionary keys.

Why is this possible?
Tuples are hashable, meaning they can be used in hash-based data structures like dictionaries. 
This is because tuples are immutable, and their hash value is determined by their contents.

Is it good practice?
Using tuples as dictionary keys can be good practice when:

- You need to use multiple values as a single key.
- The values are immutable and can be hashed.

However, it may not be suitable when:

- The values are complex or difficult to understand.
- The tuple is very large or complex.

Example
Create a dictionary with tuples as keys

"""

student_grades = {
    ('John', 'Math'): 85,
    ('John', 'Science'): 90,
    ('Alice', 'Math'): 95,
    ('Alice', 'Science'): 88
}

# Access a value using a tuple key
print(student_grades[('John', 'Math')])  # Output: 85

# Update a value using a tuple key
student_grades[('John', 'Math')] = 90
print(student_grades[('John', 'Math')])  # Output: 90

# Add a new key-value pair
student_grades[('Bob', 'Math')] = 80
print(student_grades)
#Output: {('John', 'Math'): 90, ('John', 'Science'): 90, 
# ('Alice', 'Math'): 95, ('Alice', 'Science'): 88, ('Bob', 'Math'): 80}

