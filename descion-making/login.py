# ✅ 3. Login System with Password and OTP

# Task:
# Ask for password.
# If password is correct:
# Ask for OTP
# If OTP is correct → "Login successful"
# Else → "Incorrect OTP"
# Else → "Incorrect password"

db_password = "arun123"

db_otp = 1234

password = input("enter the password ")

if password == db_password:
    otp = int(input("enter the otp"))

    if otp == db_otp:
        print("login is successfull")
    else:
        print("incorrect otp ")
else:
    print("incorrect password")
    