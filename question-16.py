def count_characters(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def main():
    input_string = input("Enter a string: ")
    
    character_frequency = count_characters(input_string)
    
    print("Character frequencies in the string:")
    for char, count in character_frequency.items():
        print("'{char}' : {count}")
main()