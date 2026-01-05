class Fibinocci:

    def solution(self,num):

        p=0
        c=1

        print(p)
        print(c)

        for _ in range (1,num-1):

            n=p+c
            print(n)
            p=c
            c=n


fib_instance=Fibinocci()

fib_instance.solution(5)


            



