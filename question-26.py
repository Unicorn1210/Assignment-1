def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix

def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")
    
    starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)
    
    print("Starts with '{prefix}': {starts_with_prefix}")
    print("Ends with '{suffix}': {ends_with_suffix}")
main()