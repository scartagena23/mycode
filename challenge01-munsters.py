#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------

# Display the value mapped to names
print("Character names: ", munsters["names"])

#Display the value mapped to endDate
print("End date of: ", munsters["endDate"])

# Display the value mapped to startDate
print("Start date of: ", munsters["startDate"])

# Add a new key, episodes mapped to the value of 70
munsters["episodes"] = 70
print(munsters["episodes"]) 
