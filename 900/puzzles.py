# https://codeforces.com/problemset/problem/337/A

nk = list(map(int, input().split()))

lis = list(map(int, input().split()))

lis.sort()

if((nk[0] % 2 == 0 and nk[1] % 2 == 0) or (nk[0] % 2 == 1 and nk[1] % 2 == 1)):
    while(len(lis) > nk[0]):
        lis.pop(0)
        lis.pop(-1)
    print(lis[-1]-lis[0])
else:
    if(abs(lis[0]-lis[1]) > abs(lis[-1]-lis[-2])):
        lis.pop(0)
        while (len(lis) > nk[0]):
            lis.pop(0)
            lis.pop(-1)
    else:
        lis.pop(-1)
        while (len(lis) > nk[0]):
            lis.pop(-1)
            lis.pop(0)
    print(lis[-1]-lis[0])


# 10 12 10 7 5 22
# after sort
# 5 7 10 10 12 22 23
# 5 7 10 10 12 22 23

# 2
# 7 7 8


# 4 4
# 1 2 3 4

# 2 3
# 4 10 290

# 1 5
# 10 11 13 14 15

# 7 10 10 12
