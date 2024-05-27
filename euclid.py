a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

def euclid(a,b):
    if a < b:
        a, b = b, a
    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
    return int(a) 

def mutually_prime(a,b):
    gcd = euclid(a,b)
    if gcd ==1:
        return True
    else:
        return False

print("最大公約数:", euclid(a, b))

print("互いに素であるか:", mutually_prime(a, b))
    