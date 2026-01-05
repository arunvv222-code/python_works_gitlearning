
#lambda = anonymous function with single expression

add_numbers=lambda n1,n2:n1+ n2

# print(add_numbers(100,200))

square=lambda n:n**2

# print(square(5))

odd_number=lambda n: True if n%2!=0 else False

# print(odd_number(23))

is_negative=lambda n : True if n<0 else False

# print(is_negative(-2))

is_century_year=lambda n: True if n%100==0 else False

print(is_century_year(2021))