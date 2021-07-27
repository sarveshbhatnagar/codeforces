lis = []
row = 0
col = 0
for i in range(5):
    lis.append(input().split())
    if("1" in lis[-1]):
        row = i+1
        col = lis[-1].index("1") + 1


print(abs(row - 3) + abs(col - 3))
