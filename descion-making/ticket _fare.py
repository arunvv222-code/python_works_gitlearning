
# ✅ 5. Ticket Fare Based on Age

# 📌 Rules:

# Age < 5 → Free
# Age 5–18 → ₹10
# Age 19–60 → ₹20
# Age > 60 → ₹15

# 🧪 Input:

# Enter your age: 70
# 📤 Output:
# Your ticket fare is ₹15.

age = int(input("enter your age "))

if age < 5:
    print("free")

elif( age in range(5,19)):
    print("10")

elif(age in range(19,61)):
    print("20")

elif age> 60:
    print("30")