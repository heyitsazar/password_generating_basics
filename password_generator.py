import random
# for getting all lower/uppercase letters, numbers, characters
import string


def generatePassword(pass_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters # we're going to have letters everytime in our passwords
    
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < pass_length:
        new_char = random.choice(characters)
        pwd += new_char

        # for checking if our password has numbers/special characters 
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers != has_number:
            meets_criteria = False
        if special_characters != has_special:
            meets_criteria = False
    return pwd

# getting user input, checking if they want numbers/special characters in their password
pass_length = int(input("Enter the desired length of generated password: "))
numbers = input("Do you want numbers in your generated password (y/n): ").lower() == "y"
special_characters = input("Do you want special characters in your generated password (y/n): ").lower() == "y"

# generating and printing
pwd = generatePassword(pass_length, numbers, special_characters)
print(pwd)