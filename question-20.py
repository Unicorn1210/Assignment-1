def sum_of_numbers(num_list):
    total = 0
    for num in num_list:
        total += num
    return total

def main():
    num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
    total_sum = sum_of_numbers(num_list)
    print("Sum of numbers:", total_sum)
main()