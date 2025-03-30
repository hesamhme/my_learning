def is_greater(a, b):
    if a > b:
        return True
    return False

numbers = input()
a, b = map(int, numbers.split())
print(is_greater(a, b))   