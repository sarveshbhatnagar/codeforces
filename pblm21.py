n = int(input())
current = "N"
ngroups = 0
for i in range(n):
    inp = input()
    if(inp[0] != current):
        ngroups += 1
        current = inp[0]
print(ngroups)
