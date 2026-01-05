def display_number(limit):

    if limit==0:

        return 
    print(limit,end=" ")

    return display_number(limit-1)

# display_number(10)

display_number(15)