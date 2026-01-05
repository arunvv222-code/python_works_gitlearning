def  grade(mark):
        if mark >= 90:
            return "A"
        elif mark >= 75:
            return "B"
        elif mark >= 50:
            return "C"
        else:
            return"F"

print(grade(20))
print(grade(95))
print(grade(75))