n = int(input())
x = int(input())

if (1<=n<=20) and (1<=x<=1000):
    for _ in range(n):
            if x % 2 == 0:
                x //= 2
            else:
                x = x * 2 - 1
print(x)