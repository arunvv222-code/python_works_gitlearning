def min_two(n1,n2):
    if n1<n2:
        return n1
    else:
        return n2

# print(min_two(10,20))


def min_two(n1,n2):
    return n1 if n1<n2 else n2
def max_two(n1,n2):

    return n1 if n1>n2 else n2
# print(min_two(100,200),"is min")
# print(max_two(100,200),"is max")


# create a function for is_oddd

    #  def is_odd(n):
    #      return True if n%2!=0 else False

    # print(is_odd(8))

#last digit max of two

def last_digit_max(n1,n2):
    return n1 if n1%10 > n2%10 else n2
# print(last_digit_max(126,245))


def is_leap_year(year):
    return True if year%100==0 and year%400==0 or year%100!=0 and year%4==0 else False
# print(is_leap_year(2003))

def bmi(height,weight):
    height_meter=height/100

    result = weight/height_meter**2

    return result
# print(bmi(165,70))

def is_perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
# print(is_perfect_number(27))
# print(is_perfect_number(34))
# print(is_perfect_number(6))

def is_prime(number):
   
    flag=True
    for i in range(2,number):
        if number%i==0:
            flag = False
            break

    return flag
print(is_prime(7))







