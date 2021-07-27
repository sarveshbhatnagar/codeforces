vals = list(map(int, input().split()))
res = vals[0]
for i in range(vals[1]):
    if(res % 10 == 0):
        res /= 10
    else:
        res -= 1

print(int(res))
