# https://codeforces.com/problemset/problem/337/A

nk = list(map(int, input().split()))

lis = list(map(int, input().split()))

lis.sort()

mini = 100000
for i in range(nk[1]-nk[0]+1):
    d = lis[i + nk[0]-1] - lis[i]
    if d < mini:
        mini = d
print(mini)


# while(len(lis) > nk[0]):
#     if(abs(lis[1]-lis[-1]) < abs(lis[0]-lis[-2])):
#         lis.pop(0)
#     else:
#         lis.pop(-1)

# print(lis)
# print(lis[-1]-lis[0])

# if((nk[0] % 2 == 0 and nk[1] % 2 == 0) or (nk[0] % 2 == 1 and nk[1] % 2 == 1)):
#     while(len(lis) > nk[0]):
#         lis.pop(0)
#         lis.pop(-1)
#     print(lis[-1]-lis[0])
# else:
#     if(abs(lis[1]-lis[-1]) > abs(lis[-2]-lis[0])):
#         lis.pop(0)
#         while (len(lis) > nk[0]):
#             lis.pop(0)
#             lis.pop(-1)
#     else:
#         lis.pop(0)
#         while (len(lis) > nk[0]):
#             lis.pop(-1)
#             lis.pop(0)
#     print(lis[-1]-lis[0])


# 10 12 10 7 5 22


# after sort
# 5 7 10 10 12 22
# d = 5

# to choose = 4
# we have = 6

# 6-4+1

# 5 7 10 10 12 22

# 7-22 = 15
# 5-12 = 7
