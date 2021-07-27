a = list(map(int, input().split()))

b = list(map(int, input().split()))

count = 0
val = b[a[1]-1]
if(val > 0):
    for i in b[a[1]:]:
        if(i == val):
            count += 1
        else:
            break
    print(count + a[1])
else:
    numz = b[a[1]-1::-1].count(0)
    print(a[1] - numz)
