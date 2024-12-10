# Function to compute Fibonacci series using a recursive approach
def fibonacci(n):
    # Handles base cases for the Fibonacci sequence
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive formula: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)

# Function to display multiple Fibonacci numbers based on user input
def generate_fibonacci_series():
    # Ask the user for the number of Fibonacci terms to generate
    terms = int(input("Enter the number of terms to display in the Fibonacci series: "))
    
    # Validate the input to ensure a positive integer is entered
    if terms <= 0:
        print("Please enter a valid positive number of terms.")
    else:
        print(f"Displaying the first {terms} terms of the Fibonacci series:")
        # Loop to print each Fibonacci number in the series
        for count in range(terms):
            print(fibonacci(count), end=" ")

# If this script is run directly, execute the series generation function
if __name__ == "__main__":
    generate_fibonacci_series()
