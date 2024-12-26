## Password Complexity Checker ###
import string
print('***Password Complexity Checker***')
# Prompt the user to enter a password
password = input('Enter password: ')

# Check if the password contains at least one uppercase letter
upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])

# Check if the password contains at least one lowercase letter
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])

# Check if the password contains at least one special character
special = any([1 if c in string.punctuation else 0 for c in password])

# Check if the password contains at least one digit
digits = any([1 if c in string.digits else 0 for c in password])

# Combine the individual checks into a list for evaluation
characters = [upper_case, lower_case, special, digits]

# Calculate the length of the password
length = len(password)

# Initialize the score variable
score = 0

# Add to the score based on the length of the password
if length > 8:
    score += 1  # Add 1 point if length is greater than 8
if length > 12:
    score += 1  # Add 1 point if length is greater than 12
if length > 17:
    score += 1  # Add 1 point if length is greater than 17
if length > 20:
    score += 1  # Add 1 point if length is greater than 20

# Add to the score based on the variety of character types used
if sum(characters) > 1:
    score += 1  # Add 1 point if there are at least 2 types of characters
if sum(characters) > 2:
    score += 1  # Add 1 point if there are at least 3 types of characters
if sum(characters) > 3:
    score += 1  # Add 1 point if all 4 types of characters are used

# Determine the password strength based on the score
if score < 4:
    print('password is weak')  # Score less than 4 indicates a weak password
elif score == 4:
    print('password is ok')  # Score of 4 indicates an acceptable password
elif score > 4:
    print('password is pretty good')  # Score greater than 4 indicates a good password
elif score > 8:
    print('password is strong')  # Score greater than 8 indicates a strong password
