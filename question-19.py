import string

def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string

def main():
    input_string = input("Enter a string with punctuation: ")
    cleaned_string = remove_punctuation(input_string)
    print("String after removing punctuation:", cleaned_string)
main()