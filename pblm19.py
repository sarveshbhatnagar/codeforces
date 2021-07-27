n = int(input())
count = 0
for i in range(n):
    pq = list(map(int, input().split()))
    if pq[1] - pq[0] >= 2:
        count += 1
print(count)
