# Function to calculate Fibonacci series using recursion
def fib(n):
    # Base case: fib(0) = 0, fib(1) = 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: fib(n) = fib(n-1) + fib(n-2)
        return fib(n - 1) + fib(n - 2)

# Main function to generate and display multiple Fibonacci numbers
def main():
    # User input for the number of terms in the Fibonacci series
    num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
    
    # Check for non-negative input
    if num_terms <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"Fibonacci series up to {num_terms} terms:")
        for i in range(num_terms):
            # Display each Fibonacci number in the series
            print(fib(i), end=" ")

# Calling the main function
if __name__ == "__main__":
    main()
