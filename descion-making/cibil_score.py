cibil = int(input("enter the cibil score "))

if cibil in range(300,551):
    print("poor")
elif cibil in range(550,651):
    print("average")
elif cibil in range(650,751):
    print("good")
elif cibil in range(750,901):
    print("excelent")
else:
    print("invalid")