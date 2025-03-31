total_price = int(input())

if total_price >= 50000:
    off_amount = total_price * 0.2
    total_price -= off_amount
    print(int(total_price))
elif 20000 < total_price < 50000:
    off_amount = total_price * 0.1
    total_price -= off_amount
    print(int(total_price))
elif total_price < 20000:
    print(int(total_price))
else:
    None

