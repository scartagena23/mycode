#!/usr/bin/env python3
## create file object in "r"ead mode

# customization 4
configfile = input("What file do you need to read?" )

with open(configfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

# customization3 option 1
count = 0
for item in configlist:
    count += 1
print(f"There are {count} lines in this file")

# customization3 option 2
num_lines = len(configlist)
print(f"This file has {num_lines} lines")

# customization3 option 3
print(f"Single line code, tells us that there is {len(configlist)} lines on this file")


