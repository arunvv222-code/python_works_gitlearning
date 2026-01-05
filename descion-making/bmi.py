height = int(input("enter the height in cm "))
weight = int(input("enter the weight in kg "))

height_in_meter = height / 100

bmi = (weight / (height_in_meter**2))

bmi = round(bmi,0)

print(bmi)



if(bmi < 20):
    print("under weight")

elif(bmi>=20 and bmi<25):
    print("normal weight")

elif(bmi>=25 and bmi<30):
    print("over weight")

elif(bmi>=30):
    print("obsess")

