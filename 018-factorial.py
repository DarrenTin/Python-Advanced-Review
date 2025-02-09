# Iterative approach to calculate factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive approach to calculate factorial
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Main program
if __name__ == "__main__":
    # Input: Number to calculate factorial
    num = int(input("Enter a number to calculate its factorial: "))

    # Choose the method (iterative or recursive)
    method = input("Choose the method (iterative/recursive): ").lower()

    if method == 'iterative':
        result = factorial_iterative(num)
        print(f"The factorial of {num} using iterative method is: {result}")
    elif method == 'recursive':
        result = factorial_recursive(num)
        print(f"The factorial of {num} using recursive method is: {result}")
    else:
        print("Invalid method choice. Please choose 'iterative' or 'recursive'.")
