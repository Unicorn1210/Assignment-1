def count_occurrences(num_list, element):
    count = 0
    for num in num_list:
        if num == element:
            count += 1
    return count

def main():
    num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
    element = int(input("Enter the element to count: "))
    occurrences = count_occurrences(num_list, element)
    print("Occurrences of {element} in the list:", occurrences)
main()