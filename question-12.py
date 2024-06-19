def sum_of_digits(number):
    # Initialize sum to zero
    sum_digits = 0
    
    # Convert number to absolute to handle negative numbers
    number = abs(number)
    
    # Iterate through each digit in the number
    while number > 0:
        # Add the last digit (remainder when divided by 10) to sum
        sum_digits += number % 10
        # Remove the last digit from number
        number //= 10
    
    return sum_digits

def main():
    number = int(input("Enter a number to calculate the sum of its digits: "))
    digit_sum = sum_of_digits(number)
    print("The sum of the digits of {number} is: {digit_sum}")

main()