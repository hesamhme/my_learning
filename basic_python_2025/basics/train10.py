# n = int(input())

# while n != 1:
#     if n % 2 == 0:
#         n //= 2
#     else:
#         n = n * 3 + 1
#     print(n)


# res = "zoj" if n % 2 == 0 else "fard"
# print(res)    
ls = [1, 2, 4, 5, 6, 7, 8, 9, 10]

new_ls = [i for i in ls if i % 2 == 0]
print(new_ls)