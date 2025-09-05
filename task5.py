# Function to calculate factorial using a loop
def factorial_loop(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Function to calculate factorial using recursion
def factorial_recursive(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Sample number to calculate factorial
sample_number = 7

# Calling the factorial functions and printing the results
print(f"Factorial of {sample_number} using loop: {factorial_loop(sample_number)}")
print(f"Factorial of {sample_number} using recursion: {factorial_recursive(sample_number)}")

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
