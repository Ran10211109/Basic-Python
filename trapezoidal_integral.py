from math import sin, pi
f_str = input("function")
f = eval(f_str)
a = int(input("range_min"))
b_str = input("range_max")
b = eval(b_str)
n = int(input("n"))


def trapezoidal_integral(f,a,b,n):
    h = (b - a) / n
    s = 0
    for k in range(1, n+1):
        s += h / 2 * (f(a + (k - 1) * h) + f(a + k * h))
    return s

result = trapezoidal_integral(f,a,b,n)
print("答えは{}".format(result))
