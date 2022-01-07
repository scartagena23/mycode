#!/usr/bin/env python3
  
# Write a Python function to find the Max of three numbers.
def findmax(num1, num2, num3):
    numlist = [num1, num2, num3]
    return max(numlist)

print(findmax(25, 100, -1))


# Write a Python function to sum all the numbers in a list.
def findsum(numbers):
    result = 0
    #iterating each number on the list
    for nums in numbers:
        result += nums
    return result

print(findsum((5, 25, 1, 50, 30))) 

# Write a Python program to print the even numbers from a given list.
def even_num(numbers):
    # initialize a new list
    result = []
    for nums in numbers:
        if nums %2 == 0:
            result.append(nums) # #append to the new list of only even numbers
    return result

print(even_num([1,2,3,4,5,6,7,8,9,10,11,12]))

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_elems(elements):
    # initialize the empty list
    unique_elements = []
    # iterate each element of the list
    for elems in elements:
        # validate if they exist
        if elems not in unique_elements:
            unique_elements.append(elems) #append to the new list with unique elements
    return unique_elements

print(unique_elems([1,2,3,3,3,3,4,5]))

