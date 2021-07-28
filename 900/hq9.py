# https://codeforces.com/problemset/problem/133/A

sample = {"H", "Q", "9", }
s = set(list(input()))

if(s.intersection(sample) != set()):
    print("YES")
else:
    print("NO")
