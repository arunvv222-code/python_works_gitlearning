class Numbercount:

    def solution(*args,**kwargs):

        val=kwargs.get("values")

        lst=list(args)

        count=lst.count(val)

        return count
    
num_count=Numbercount()

print(num_count.solution(10,10,30,40,40,values=10))

