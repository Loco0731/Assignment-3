# # Task 1: Calculate Factorial Using a Function 
#     # Problem Statement: Write a Python program that:
#     # 1.Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#     # 2.Returns the calculated factorial.
#     # 3.Calls the function with a sample number and prints the output.
    
def factorial(n):
    if n<0:
        return "Factorial is not defined for negative numbers."
    result = 1 
    for i in range(1,n+1):
        result *= i
    return result
    
num = 5
print(f"Factorial of {num} is:", factorial(num))

# Task 2: Using the Math Module for Calculations
    # Problem Statement: Write a Python program that:
    # 1.   Asks the user for a number as input.
    # 2.   Uses the math module to calculate the:
        # Square root of the number
        # Natural logarithm (log base e) of the number
        # Sine of the number (in radians)
    # 3.   Displays the calculated results.

import math

n = int(input("Enter The Value Of n: "))

square_root = math.sqrt(n) if n >= 0 else "Square root cannot define the negative numbers"
natural_log = math.log(n) if n > 0 else "Natural logarithm is not defined for non-positive numbers"
sine = math.sin(n)

print("The value of square root is : ",square_root)
print("The value of natural logorithm is : ",natural_log)
print("The value of Sine is : ",sine)