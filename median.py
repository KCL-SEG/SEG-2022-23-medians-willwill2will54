"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        numbers.sort() # Sort the list
        middle = len(numbers) // 2 # Get middle index

        if len(numbers) % 2 == 1:
            middle_num = numbers[middle]
        else:
            middle_num = (numbers[middle] + numbers[middle - 1]) / 2
        print(middle_num) # Print value at middle index
        break
