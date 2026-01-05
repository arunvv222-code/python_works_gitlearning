number=15

is_prime=not any([number%i==0 for i in range(2,number)])

print(is_prime)