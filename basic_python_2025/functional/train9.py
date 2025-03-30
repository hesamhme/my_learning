def skyline(*args):
    highest = 0
    for building in args[0]:
        if building > highest:
            highest = building
    return highest

buildings = input()
buildings = list(map(int, buildings.split()))
print(skyline(buildings))