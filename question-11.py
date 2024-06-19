def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to nth number
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_numbers = generate_fibonacci(n)
        print("The first {n} Fibonacci numbers are:")
        print(fibonacci_numbers)
main()