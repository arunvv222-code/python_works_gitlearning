def fibnoci(number):
    fab_num=[]
    p=0
    c=1
    n=p+c

    while n<=number:
        p=c
        c=n
        n=p+c

    return n ,fibnoci(number-1)

print(fibnoci(10))
