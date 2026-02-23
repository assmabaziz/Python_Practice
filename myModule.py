import datetime


def print_name(name):
    print(f"Hello {name}")


def print_age():
    currentYear = datetime.datetime.now().year
    birthYear = input("Please enter your birth year:  ")
    age = currentYear - int(birthYear)
    if age > 18  :
        print(f"Hello adult, your age is:  {age}")
    elif age < 18 and age > 0:
        print(f"Hello teenager, your age is: {age}")
    elif age == 0 or birthYear >= 2026 : 
        print("Did you drink your coffee?")

