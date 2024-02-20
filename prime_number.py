# TODO
n = float(input("number,please"))

def prime_number(a):
    if a < 0:
        print("正の値で入力してください")
        return False
    n = int(a)
    if a - n != 0:
        print("整数の値を入力してください")
        return False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
            
    if count == 2:
        print("素数です")
        return True
    else:
        print("素数じゃない")
        return False
    
prime_number(n)