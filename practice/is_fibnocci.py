class Fabinocci:

    def solution(self,number):

        is_fabinocci=True

        fab_numbers=[]

        p=0
        c=1

        fab_numbers.append(p)
        fab_numbers.append(c)

        for _ in range(1,number+1):

            n=p+c
            fab_numbers.append(n)
            p=c
            c=n

        if number not in fab_numbers:

            is_fabinocci=False

        print(is_fabinocci)


    def solution_2(self,number):

        is_fab=False

        p=0
        c=1
        n=p+c

        while n<=number:

            n=p+c
            p=c
            c=n

            if n==number:
                is_fab=True


        return is_fab



is_fab_inst=Fabinocci()
is_fab_inst_2=Fabinocci()

# is_fab_inst.solution(15)
print(is_fab_inst_2.solution_2(15))