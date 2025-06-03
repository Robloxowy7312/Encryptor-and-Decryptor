import sys
import string

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)

while True:
    try:
        choice = input("Do you want to encrypt or decrypt? (E or D) ").upper()
    except Exception:
        print("Error! Please try again.")
    else:
        if choice == "E" or choice == "D":
            break
        else:
            print("Invalid choice! Enter E or D.")

if choice == "E":
    while True:
        try:
            text = input("Enter the text to encrypt: ")
        except Exception:
            print("Error! Please try again.")
        else:
            break
elif choice == "D":
    while True:
        try:
            text = input("Enter the text to decrypt: ")
        except Exception:
            print("Error! Please try again.")
        else:
            break
else:
    print("Invalid choice!")
    sys.exit(2)

result = ""
if choice == "E":
    for char in text:
        if char in lowercase_letters:
            index = lowercase_letters.index(char)
            new_index = (index + 13) % 26
            result += lowercase_letters[new_index]
        elif char in uppercase_letters:
            index = uppercase_letters.index(char)
            new_index = (index + 13) % 26
            result += uppercase_letters[new_index]
        else:
            result += char
elif choice == "D":
    for char in text:
        if char in lowercase_letters:
            index = lowercase_letters.index(char)
            new_index = (index - 13) % 26
            result += lowercase_letters[new_index]
        elif char in uppercase_letters:
            index = uppercase_letters.index(char)
            new_index = (index - 13) % 26
            result += uppercase_letters[new_index]
        else:
            result += char

print("Result:", result)
