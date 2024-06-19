def check_anagram(str1, str2):
    # Remove spaces and convert to lowercase for case insensitivity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if lengths are different
    if len(str1) != len(str2):
        return False
    
    # Count frequency of each character in both strings
    char_count1 = {}
    char_count2 = {}
    
    for char in str1:
        if char in char_count1:
            char_count1[char] += 1
        else:
            char_count1[char] = 1
    
    for char in str2:
        if char in char_count2:
            char_count2[char] += 1
        else:
            char_count2[char] = 1
    
    # Compare the dictionaries
    return char_count1 == char_count2

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    
    if check_anagram(str1, str2):
        print("'{str1}' and '{str2}' are anagrams.")
    else:
        print("'{str1}' and '{str2}' are not anagrams.")
main()