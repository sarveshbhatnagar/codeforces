a = []
for i in range(5):
    a.append(int(input()))

count = 0
for i in range(1, a[-1]+1):
    if(i % a[0] == 0 or i % a[1] == 0 or i % a[2] == 0 or i % a[3] == 0):
        count += 1

print(count)
