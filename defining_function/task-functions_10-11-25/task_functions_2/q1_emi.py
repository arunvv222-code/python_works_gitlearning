def emi(amount,tenure,rate):
    rate=rate/(12*100)
    
    result = amount*rate*(1+rate)**tenure/((1+rate)**tenure-1)

    return round (result)
print(emi(10000,12,5))