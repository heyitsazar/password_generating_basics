# Password Generator

This Python script generates a random password based on user-defined criteria such as length, inclusion of numbers, and special characters.

## Usage

1. Clone the repository or download the `password_generator.py` file.
2. Run the script using Python.
3. Follow the prompts to specify the desired length and character types for the password.
4. The generated password will be displayed on the console.

## How it Works

The script utilizes the `random` and `string` modules in Python to generate random passwords. It allows users to define the length of the password and specify whether they want numbers and special characters included.

## Function: generatePassword

This function takes three parameters:
- `pass_length`: Length of the password to be generated.
- `numbers`: Boolean value indicating whether numbers should be included in the password.
- `special_characters`: Boolean value indicating whether special characters should be included in the password.

The function generates a password by selecting characters randomly from the pool of lowercase and uppercase letters, numbers, and special characters (if specified). It ensures that the generated password meets the specified criteria.

## Example

```python
pass_length = int(input("Enter the desired length of the generated password: "))
numbers = input("Do you want numbers in your generated password (y/n): ").lower() == "y"
special_characters = input("Do you want special characters in your generated password (y/n): ").lower() == "y"

# Generate and print the password
pwd = generatePassword(pass_length, numbers, special_characters)
print(pwd)
```

## Example Output

```
Enter the desired length of the generated password: **12**
Do you want numbers in your generated password (y/n): **y**
Do you want special characters in your generated password (y/n): **n**
Generated Password: **vZ6cWu8FpYr4**
```

**Note:** This project serves as an educational resource to demonstrate basic password generation techniques in Python. It covers concepts such as randomization, string manipulation, user input handling, and conditional statements.
