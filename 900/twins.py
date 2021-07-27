# https://codeforces.com/problemset/problem/160/A

n = input()
a = list(map(int, input().split()))
a.sort(reverse=True)

for i in range(len(a)):
    if(sum(a[:i+1]) > sum(a[i+1:])):
        print(len(a[:i+1]))
        break
