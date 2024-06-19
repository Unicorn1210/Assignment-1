def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

def main():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to check for: ")
    
    if check_substring(main_string, substring):
        print("The substring '{substring}' is present in the main string.")
    else:
        print("The substring '{substring}' is not present in the main string.")
main()