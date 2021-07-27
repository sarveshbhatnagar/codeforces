# https://codeforces.com/problemset/problem/96/A

n = input()

count = 1

current = -1
previous = -2
flag = False

for i in range(len(n)):
    current = n[i]
    if current == previous:
        count += 1
    else:
        previous = current
        count = 1
    if(count >= 7):
        flag = True
        break

if(flag):
    print("YES")
else:
    print("NO")
