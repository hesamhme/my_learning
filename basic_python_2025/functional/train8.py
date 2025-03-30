def pick_evens(*args):
    evens = []
    for number in args[0]:
        if number % 2 == 0:
            evens.append(number)
    return evens

numbers = input()
numbers = list(map(int, numbers.split()))
print(pick_evens(numbers))
