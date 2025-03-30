def sum_of_squares(a, b):
    return a**2 + b**2

numbers = input()
a, b = map(int, numbers.split())
result = sum_of_squares(a, b)
print(result)