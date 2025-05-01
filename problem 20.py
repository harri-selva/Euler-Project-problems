import math

# We calculate the sum of the digits of the factorial of 100 using a different method
def compute():
    # Calculate the factorial of 100 using the math library
    n = math.factorial(100)
    
    # Initialize a variable to store the sum of digits
    digit_sum = 0

    # Convert the factorial to a string to iterate through each character (digit)
    for digit in str(n):
        # Add the integer value of each character (digit) to the sum
        digit_sum += int(digit)

    # Return the result as a string
    return str(digit_sum)


if __name__ == "__main__":
    print(compute())