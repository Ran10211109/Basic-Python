a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
if a < b:
    a, b = b, a
while True:
    r = a % b
    if a < b:
        q = a // b
        a = b*q + r
        a = b
        b = r
    if r == 0:
        print("最大公約数は{}です。".format(q))
        break