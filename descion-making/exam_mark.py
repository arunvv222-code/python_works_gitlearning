
# 3. Exam Marks – Pass and Distinction

# Task:
# Ask for marks out of 100.
# If marks ≥ 40 → "Pass"
# .
# .
# If marks ≥ 90 → "Distinction"
# Else → "Fail"

mark = int(input("enter the mark out of 100 ")) 

if( 40 <= mark <=90):
    print("pass")
elif(mark >= 90):
    print("Distinction")
else:
    print("fail")
