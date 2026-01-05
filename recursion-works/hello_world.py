"""
recurstion is the function call itself repeatedly
"""


def display_hello_world(limit):

    if limit==0:

        return
    
    print("Hello World")

    return  display_hello_world(limit-1)


display_hello_world(5)