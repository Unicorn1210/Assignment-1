def main():
    lines = []
    
    print("Enter multiple lines of text. Press Enter without typing anything to finish:")
    
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    print("\nLines entered:")
    for line in lines:
        print(line)
main()