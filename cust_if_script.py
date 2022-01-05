#!/usr/bin/env python3

# Determine a persons generation based on their age

message = 'Based on your age, as of today,  you are part of generation: '

# request user input for their age
age = int(input("How old are you? "))

# Return the generation based on the age input
if age >= 94:
    message = 'No generation information available'
elif age >= 75:
    message = message + 'The Silent Generation.'
elif age >= 57:
    message = message + 'Baby Boomers'
elif age >= 41:
    message = message + 'Generation X'
elif age >= 25:
    message = message + 'Millennials'
elif age >= 9:
    message = message + 'Generation Z'
elif age >= 0:
    message = message + 'Generation Alpha'
print(message)

