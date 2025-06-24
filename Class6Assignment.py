"""

Define a function called person that takes in the
following positional arguments first_name,
middle_name, last_name and the following
keyword arguments sex, age. 
The function should return all the data supplied.
Remember to pass the appropriate arguments
when calling your function

"""

# Person Function

def person(first_name, middle_name, last_name, sex, age):
    """
        first_name (str): First name of the person.
        middle_name (str): Middle name of the person.
        last_name (str): Last name of the person.
        sex (str): Sex of the person (keyword-only).
        age (int): Age of the person (keyword-only).
    
    Returns:
        dict: Dictionary containing person's details.
    """
    return {
        "First Name": first_name,
        "Middle Name": middle_name,
        "Last Name": last_name,
        "Sex": sex,
        "Age": age
    }

# Call the function
person_details = person("Akorede", "Sunday", "Fowowe", sex="Male", age=24)
print(person_details)
