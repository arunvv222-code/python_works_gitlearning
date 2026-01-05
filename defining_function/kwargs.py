# def display_person(**kwargs):

#     # print(kwargs)

# display_person(name="arun",age=22,n_place="kkm",w_place="london",salary=2000000)


def operation(*args,**kwargs):

    op=kwargs.get("key")

    if op == "max":
        return max(args)
    else:
        return min(args)

print(operation(10,20,30,40,key="max"))
print(operation(10,20,30,40,key="min"))