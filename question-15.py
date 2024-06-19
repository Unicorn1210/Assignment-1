import csv

def main():
    file_name = input("Enter the CSV file name (e.g., data.csv): ")
    
    try:
        with open(file_name, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            
            print("Contents of the CSV file '{file_name}':")
            for row in csv_reader:
                print(', '.join(row))
                
    except FileNotFoundError:
        print("Error: The file '{file_name}' was not found.")
    except Exception as e:
        print("Error reading the file: {e}")
main()