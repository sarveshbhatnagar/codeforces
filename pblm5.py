n = int(input())
x = 0
for i in range(n):
    inp = input()
    if("+" in inp):
        x += 1
    else:
        x -= 1
print(x)
