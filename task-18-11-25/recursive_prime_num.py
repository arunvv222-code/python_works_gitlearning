number=[2,4,5,10,13,14,13,11,7,9,7]

prime_numbers={}

for num in number:
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime=False
    if is_prime:
        if num in prime_numbers:
            prime_numbers[num]+=1
        else:
            prime_numbers[num]=1

for k,v in prime_numbers.items():
    if v>1:
        print(k)
