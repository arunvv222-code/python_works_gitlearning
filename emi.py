prinicaple_amount = int(input("enter the princaple amount : "))

rate_of_intrest = int(input("enter the rate of intrest : "))

number_of_monthly_installment = int(input("enter the number of installment : "))

rate = rate_of_intrest / (12 *100)

emi_amount= ((prinicaple_amount*rate*(1+rate)**number_of_monthly_installment)/ ((1+rate)**number_of_monthly_installment-1))

print("emi amount is :",emi_amount)