# https://codeforces.com/problemset/problem/580/A

n = int(input())
lis = list(map(int, input().split()))

prev = -1
count = 0
max_count = 1
for i in range(len(lis)):
    if(prev <= lis[i]):
        count += 1
    else:
        if(max_count < count):
            max_count = count
        count = 1
    prev = lis[i]
    max_count = count if max_count < count else max_count

print(max_count)
