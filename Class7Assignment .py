"""
Write a function to find the factorial of a number
Write a function that checks if a number is prime
(limit to the first 10 prime numbers 2, 3, 5, 7, 11, 13, 17, 19, 23, 29).
Write a script that reads from a file and prints each line with line numbers
Write a script that asks the user for input and appends it to a file
"""
# Normal Method
from math import sqrt, factorial
print(factorial(4))



# FACTORIAL!

# Checking For Zero And Negative Numbers
Number = eval(input("enter a number: "))
while Number < 1:
    Number = eval(input("enter a valid number number: "))
    
# If The Number Is 1, Automaically The Factorial Is 1     
if Number == 1:
    print("The Factorial Of 1 Is 1")
    
# For Numbers Greater Than 1    
elif Number > 1:
    
    Num = Number # Storing The Number In A New Variable To Avoild Reduction.
    NumberProduct = Num * 1 # To Get The Product Of The Factorial
    
    while Num > 1:
        Num -= 1
        NumberProduct *= Num
        
    print(F"The Factorial Of {Number} Is: {NumberProduct}")


# Function

def Factorial():
    print("Factorial Function")
    Numeric = eval(input("enter a number: "))
    while Numeric < 1:
        Numeric = eval(input("enter a valid number number: "))
    
# If The Number Is 1, Automaically The Factorial Is 1     
    if Numeric == 1:
        print("The Factorial Of 1: Is 1")
    
# For Numbers Greater Than 1    
    elif Numeric > 1:
    
        Num = Numeric # Storing The Number In A New Variable To Avoild Reduction.
        NumericProduct = Num * 1 # To Get The Product Of The Factorial
    
    while Num > 1:
        Num -= 1
        NumericProduct *= Num
        
    print(F"The Factorial Of: {Numeric} Is: {NumericProduct}")
    
    
Factorial()

# PRIME NUMBERS
"""
#a whole number greater than 1 
#that cannot be exactly divided by
#any whole number other than itself and 1 
#(e.g. 2, 3, 5, 7, 11).

"""

# Checking For One, Zero And Negative Numbers
"""
PrimeNumber = eval(input("enter a prime number: "))
while PrimeNumber < 2:
    PrimeNumber = eval(input("enter a number greater than 1: "))

# if PrimeNumber // 1 == PrimeNumber and PrimeNumber // PrimeNumber == 1 and PrimeNumber % 2 != 0:
if PrimeNumber == 2:
    print(PrimeNumber, "is a prime Number")
if PrimeNumber % 2 != 0 and PrimeNumber % 2 != 1:
    print(PrimeNumber, "is a prime number.")
    
else:
    print(PrimeNumber, "is not a prime number")
    
"""    
    
# Reading And Printing Files With Numbers
file = "practice.txt"
try:
    
    with open(file, "r") as file_object:
        content = file_object.readlines()
        for index, text in enumerate(content, 1):
            print(f"Index: {index}: {text}")
            
except FileNotFoundError:
    print(F"{file} Not Found")
    
# Appending To File
file = "practice.txt"
try:
    
    with open(file, "a+") as file_object:
        user_input = input("Enter some text: ")
        file_object.write(user_input + "\n")
        

    print(F"Input Appended To {file} Successfully.")
            
except FileNotFoundError:
    print(F"{file} Not Found")
