nt = list(map(int, input().split()))
q = input()

newGroup = []
groups = []
for i in range(len(q)):
    if(q[i] == "B"):
        newGroup = []
        newGroup.append(q[i])
        groups.append(newGroup)
    else:
        if(len(groups) > 0):
            groups[-1].append(q[i])
        else:
            groups.append([q[i]])

# print(groups)

for i in range(len(groups)):
    if(len(groups[i]) > nt[1]):
        groups[i][0], groups[i][nt[1]] = groups[i][nt[1]], groups[i][0]

    else:
        val = groups[i].pop(0)
        groups[i].append(val)

# print(groups)
ngrp = ["".join(i) for i in groups]
print("".join(ngrp))


# BGBBGGGGB 3 Q
# (BGG)(B)(BGGGG)(B)

# (BGGGG)


# ...
# GBBGGGBGB 3 A

# (BG)(B)(BGGGG)B
# (GB)
