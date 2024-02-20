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
    print("最大公約数は")
    return int(a)
    
print(euclid(a,b))

def mutually_prime(a,b):
    gcd = euclid(a,b)
    if gcd ==1:
        print(f"{a}と{b}は互いに素です")
    else:
        print(f"{a}と{b}は互いに素ではない")
    