### Packages needed here:
import pandas as pd
import datetime as dt


# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
def car_at_light(light):
    action = ""
    if light=="red":
        action="stop"
    elif light=="yellow":
        action="wait"
    elif light=="green":
        action="go"
    else:
        raise Exception("Undefined instruction for color:" +light)
    return action
# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 
def safe_subtract(a,b):
    try:
        result = a-b
        return result
    except TypeError:
        return None

#print(safe_subtract(1,))

#As we can see in the e.g. if the function is missing any of the two parameters, or the two parameters we can also get the error:
#  "missing # required positional argument"

#print(safe_subtract(1,"2"))

#Additionally if the parameter added is a number but in string format, it will still show None instead of converting the parameter
#to the right type, which could be done before in the function

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def retrieve_age_lbyl(dict):
    
    dict = dict
    
    if "birth" in dict.keys():
        age = dt.datetime.now().year - dict["birth"]
        print(dict['name'] + " is " + str(age) + " years old.")
    else:
        print("The age of " +  dict['name'] + " is not available.")


retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})


def retrieve_age_eafp(dict):
    
    dict = dict
    
    try:
        age = dt.datetime.now().year - dict["birth"]
        print(dict['name'] + " is " + str(age) + " years old.")
    except KeyError:
        print("The age of " +  dict['name'] + " is not available.")
        
        
retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987})
retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'})



# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#

def read_data(file):
    
    try:
        df = pd.read_csv(file)
        print("File has been found.")
        return(df)
    except FileNotFoundError:
        print("Error: The file does not exist.")


read_data("data.csv")



# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem



# Error explanation:
# Logical mistake in updating the total:

# The purpose of the code seems to be calculating the sum of the doubled values of the elements in the list [10, 5, 2].
# However, the line total_double_sum += elem adds the original value of elem to the total, instead of adding the doubled value (double).
# Unused variable double:
# The variable double = elem * 2 is calculated but never used. The doubled value should be added to total_double_sum, not the original elem.

# Corrected code
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double  # Add the doubled value to the total

print(total_double_sum)  # Also, print the result


### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

# Error explanation:
# Resetting the strings variable inside the loop:

# In each iteration, the strings variable is being reassigned to a new value (string + "_" + string). This means that after # each iteration, the value of strings is overwritten by the latest result, and any previous values are lost.
# The intent seems to be concatenating each word in the list, with an underscore (_) separator, but the logic
# currently just overwrites the variable instead of accumulating the result.
# Concatenating each string with itself:

# The expression string + "_" + string concatenates the same word with an underscore, like "I_I", "am_am", "Groot_Groot". 
# This may not be the desired outcome, as it looks like the goal is to concatenate different words with an underscore 
# separating them.

# Corrected Code
strings = ''
for string in ['I', 'am', 'Groot']:
    if strings:  # Check if `strings` is non-empty to avoid leading underscore
        strings += "_" + string
    else:
        strings = string  # Assign the first element without underscore

print(strings)  # Output the concatenated string




### (c) Careful!
j=10
while j > 0:
   j += 1

# Error explanation:
# Infinite loop:
# The condition while j > 0: checks if j is greater than 0, which is true at the start since j = 10.
# Inside the loop, j is incremented by 1 (j += 1), so j will keep increasing, and the condition j > 0 will always remain true. 
# This results in an infinite loop, as j will never become less than or equal to 0.
# The intent might be to decrease the value of j and terminate the loop when j becomes zero or negative, 
# but the current code does the opposite.

# Corrected Code
j = 10
while j > 0:
    j -= 1  # Decrement j by 1 in each iteration

print("Loop finished, j =", j)



### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem

print(productory)


# Error explanation:
# Incorrect initialization of productory:
# The goal of the code seems to be calculating the product of the elements in the list [1, 5, 25].
# However, the variable productory is initialized to 0. 
# When you multiply any number by 0, the result is always 0. So, multiplying productory by any of the elements in the list will result in 0 on every iteration.
# To calculate a product, productory should be initialized to 1, not 0, because 1 is the identity element for multiplication.

# Corrected code
productory = 1
for elem in [1, 5, 25]:
    productory *= elem  # Multiply productory by each element

print(productory)  # Output the product




    