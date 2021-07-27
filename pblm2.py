n = int(input())
count = 0
for i in range(n):
    a = [int(val) for val in input().split()]
    if sum(a) >= 2:
        count += 1
print(count)
