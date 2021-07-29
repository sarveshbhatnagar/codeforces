# https://codeforces.com/problemset/problem/405/A

n = input()
l = list(map(int, input().split()))
l.sort()
l = map(str, l)
print(" ".join(l))
