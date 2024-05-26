from math import sin, pi, exp, sqrt

def trapezoidal_integral(f, a=0, b=1, n=100):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for k in range(1, n):
        s += f(a + k * h)
    return s * h

# (1) 
def f1(x):
    return sin(x)

result1 = trapezoidal_integral(f1, 0, pi / 2, 50)
print("(1) sin(x) の台形積分結果: {}".format(result1))

# (2) 
def f2(x):
    return 4 / (1 + x**2)

result2 = trapezoidal_integral(f2, 0, 1, 100)
print("(2) 4/(1+x^2) の台形積分結果: {}".format(result2))

# (3) 
def f3(x):
    return sqrt(pi) * exp(-x**2)

result3 = trapezoidal_integral(f3, -100, 100, 1000)
print("(3) sqrt(pi) * exp(-x^2) の台形積分結果: {}".format(result3))
