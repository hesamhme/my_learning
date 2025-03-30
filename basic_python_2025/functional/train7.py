
def sum_numbers(*args):
    sum_ = 0
    for number in args[0]:
        sum_ += number
    return sum_

numbers = input()
numbers = list(map(int, numbers.split()))
print(sum_numbers(numbers))


    