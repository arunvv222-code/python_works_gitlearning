

# 2. Driving License Eligibility

# Task:
# Ask for age.
# If age ≥ 18:
# Ask if test is passed (yes or no)
# If yes → "License Approved"
# Else → "Test not cleared"
# Else → "Not eligible due to age"

age = int(input("enter age "))

if age >+18:
    test = input("test passed or not ")
    if test=="yes":
        print("license is approved ")
    else:
        print("test is not passed ")
    
else:
    print("not eligible due to age")


        




