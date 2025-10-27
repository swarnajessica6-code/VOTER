# Python program to check if a person is eligible to vote or not

# Taking age as input
age = int(input("Enter your age: "))

# Checking eligibility
if age >= 18:
    print(" You are eligible to vote.")
else:
    print(" You are not eligible to vote.")
    print("You must be at least 18 years old to vote.")