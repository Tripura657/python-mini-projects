# Age Calculator
from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    today = date.today()
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    return age

if __name__ == "__main__":
    y = int(input("Enter your birth year: "))
    m = int(input("Enter your birth month: "))
    d = int(input("Enter your birth day: "))

    print(f"You are {calculate_age(y, m, d)} years old.")
