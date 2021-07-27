n = int(input())
lis = []
for i in range(n):
    if(i % 2 == 0):
        lis.append("I hate")
    else:
        lis.append("I love")
st = ""
for i in lis:
    st += i
    st += " that "
print(st[:-5] + "it")
