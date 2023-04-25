import math
class SignError(Exception):
    """Raised when the input values are with same sign"""

    pass

def func1(x):
    return pow(math.e,x) -2 * x - 2

def func2(x):
    return math.pow(x,3) + 3 * x -5

def bisection(a,b,func):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "a and b need to be numbers"

    try:
          func(a) * func(b) < 0

    except SignError:
        print("a and b should be with diferant sign")


    while (b-a) >= 0.1 :
        mid = (a+b) / 2
        if func(mid) == 0.0:
            break

        if func(mid) + func(a) < 0:
            b = mid
        elif func(mid) + func(b) < 0:
            a = mid
    return mid
a = '-1'
b = '1'
root = bisection(a,b,func1)
print(root)
