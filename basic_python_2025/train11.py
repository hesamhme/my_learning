n = int(input())

if n % 5 == 0 and n % 3 == 0:
    print("افسانه ای")
elif n % 5 == 0:
    print("نفرین شده")
elif n % 3 == 0:
    print("جادویی")
else:
    print("معمولی")