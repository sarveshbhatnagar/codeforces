n = int(input())
currentval = 0
maxval = 0
for i in range(n):
    ab = list(map(int, input().split()))
    currentval -= ab[0]
    currentval += ab[1]
    if(maxval < currentval):
        maxval = currentval

print(maxval)
