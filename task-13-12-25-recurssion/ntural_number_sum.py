
def sum_natural_num(limit):

    if limit==0:
        return 0
    
    return limit+sum_natural_num(limit-1)

print(sum_natural_num(5))



