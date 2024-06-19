def calculate_age(birth_year):
    current_year = 2024  # Replace with the current year
    age = current_year - birth_year
    return age

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
        if birth_year <= 0 or birth_year > 2024:  # Adjust based on current year
            print("Invalid birth year. Please enter a valid year.")
        else:
            age = calculate_age(birth_year)
            print("You are {age} years old.")
    except ValueError:
        print("Invalid input. Please enter a valid year (e.g., 1990).")
main()