a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))
# TODO
if a < b:
    a, b = b, a
while b != 0:
    q = a // b
    r = a % b
    a = b
    b = r
print("最大公約数は{}です。".format(a))