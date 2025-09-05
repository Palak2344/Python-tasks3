# Python-tasks3
Python scripts for basic tasks
# Task 1: Calculate Factorial Using a Function

## Problem Statement

Write a Python program that:
1. Defines a function named `factorial` that takes a number as an argument and calculates its factorial using a loop or recursion.
2. Returns the calculated factorial.
3. Calls the function with a sample number and prints the output.

## Implementation

Here is the Python code that accomplishes the above task:

```python
def factorial(n):
    """Calculate the factorial of a number using iteration."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Sample number
sample_number = 5

# Calling the factorial function and printing the result
result = factorial(sample_number)
print(f"The factorial of {sample_number} is: {result}")
```
# Task 2: Using the Math Module for Calculations

## Problem Statement

Write a Python program that:
1. Asks the user for a number as input.
2. Uses the math module to calculate the:
   - Square root of the number
   - Natural logarithm (log base e) of the number
   - Sine of the number (in radians)
3. Displays the calculated results.

## Implementation

Here is the Python code that accomplishes the above task:

```python
import math

def main():
    # Ask the user for a number
    user_input = input("Please enter a number: ")
    
    try:
        # Convert the input to a float
        number = float(user_input)
        
        # Calculate the square root
        square_root = math.sqrt(number)
        
        # Calculate the natural logarithm
        natural_log = math.log(number)
        
        # Calculate the sine (in radians)
        sine_value = math.sin(number)
        
        # Display the results
        print(f"The square root of {number} is: {square_root}")
        print(f"The natural logarithm (log base e) of {number} is: {natural_log}")
        print(f"The sine of {number} (in radians) is: {sine_value}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the main function
if __name__ == "__main__":
    main()
```
   
