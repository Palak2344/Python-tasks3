import math

# Function to perform calculations using the math module
def calculate_math_operations():
    # Asking the user for a number as input
    number = float(input("Enter a number: "))

    # Calculating square root
    square_root = math.sqrt(number)

    # Calculating natural logarithm
    if number > 0:
        natural_log = math.log(number)
    else:
        natural_log = "Undefined for non-positive numbers"

    # Calculating sine (in radians)
    sine_value = math.sin(number)

    # Displaying the results
    print(f"Square root of {number}: {square_root}")
    print(f"Natural logarithm (log base e) of {number}: {natural_log}")
    print(f"Sine of {number} (in radians): {sine_value}")

# Calling the function to execute the program
calculate_math_operations()

