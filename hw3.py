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
        return(dict['name'] + " is " + str(age) + " years old.")
    else:
        return("The age of " +  dict['name'] + " is not available.")


print(retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987}))
print(retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}))


def retrieve_age_eafp(dict):
    
    dict = dict
    
    try:
        age = dt.datetime.now().year - dict["birth"]
        return(dict['name'] + " is " + str(age) + " years old.")
    except KeyError:
        return("The age of " +  dict['name'] + " is not available.")
        
        
print(retrieve_age_lbyl({'name': 'John', 'last_name': 'Doe', 'birth': 1987}))
print(retrieve_age_lbyl({'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}))



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
        return("Error: The file does not exist.")


print(read_data("data.csv"))



# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += elem

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings = string+"_"+string

### (c) Careful!
j=10
while j > 0:
   j += 1

### (d)
productory = 0
for elem in [1, 5, 25]:
    productory *= elem
    
