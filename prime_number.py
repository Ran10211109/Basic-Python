def prime_number(a):
    if not isinstance(a, (int, float)):
        print("数値を入力してください")
        return False
    
    if a <= 0:
        print("正の値で入力してください")
        return False

    n = int(a)
    if a - n != 0:
        print("整数の値を入力してください")
        return False

    if n < 2:
        print("自然数（2 以上）を入力してください")
        return False
    
    for i in range(1, n + 1):
        if n % i == 0:
            return False
        
    return True
    
    if count == 2:
        print("素数です")
        return True
    else:
        print("素数じゃないです")
        return False

try:
    n = float(input("自然数を入力してください: "))
    prime_number(n)
except ValueError:
    print("数値を入力してください")
