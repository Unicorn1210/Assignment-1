def find_min_max(num_list):
    if not num_list:
        return None, None
    
    min_value = min(num_list)
    max_value = max(num_list)
    
    return min_value, max_value

def main():
    num_list = [int(x) for x in input("Enter numbers separated by space: ").split()]
    min_value, max_value = find_min_max(num_list)
    
    if min_value is not None and max_value is not None:
        print("Minimum value: {min_value}")
        print("Maximum value: {max_value}")
main()