# https://codeforces.com/problemset/problem/208/A

s = input()
x = s.split("WUB")
count = x.count("")
for i in range(count):
    x.remove("")
print(" ".join(x))
