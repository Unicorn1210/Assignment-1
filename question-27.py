def string_to_list(input_string):
    return list(input_string)

def main():
    input_string = input("Enter a string: ")
    char_list = string_to_list(input_string)
    print("List of characters:", char_list)
main()