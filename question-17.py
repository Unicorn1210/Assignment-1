def convert_to_title_case(input_string):
    words = input_string.split()

    capitalized_words = []

    for word in words:
        capitalized_word = word.capitalize()
        capitalized_words.append(capitalized_word)

    title_case_string = ' '.join(capitalized_words)

    return title_case_string

def main():
    input_string = input("Enter a string to convert to title case: ")
    title_case_string = convert_to_title_case(input_string)
    print("Original string:", input_string)
    print("Title case string:", title_case_string)
main()