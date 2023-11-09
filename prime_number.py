# TODO
n = 10
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("{}は素数である".format(n))
else:
    print("{}は素数ではない".format(n))

