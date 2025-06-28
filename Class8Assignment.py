# Reading From A File

try:
    filename = "example.txt"
    with open(filename, 'r') as file:
        for num, line in enumerate(file, 1):
            """
            using (,1 Or Start=1) Makes The Index Start 
            From 1 Not The Natural 0 Start Index.
            """
            print(f"{num}: {line.strip()}")
            """
            line.strip()
            
line.strip() removes any leading or trailing whitespace 
characters(like spaces, tabs, or newlines) from the line.

strip()` is used to:

1. Remove the newline character (`\n`) at the end of 
each line,so `print()` doesn't add an extra newline.
2. Clean up the output by removing any leading or
Atrailing whitespace.
            

            """
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' was not found.")
except Exception:
    print(f"An error occurred while reading '{filename}'.")

# Appending To A File
try:
    filename = "example.txt"
    user_input = "This is a test input."
    with open(filename, 'a') as file:
        file.write(user_input + "\n")
    print(f"Input appended to '{filename}' successfully.")
except PermissionError:
    print(f"Sorry, you don't have permission to write to '{filename}'.")
except Exception:
    print(f"An error occurred while writing to '{filename}'.")