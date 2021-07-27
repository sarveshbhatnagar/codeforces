nq = list(map(int, input().split()))

s = input()

chardic = dict()
sample = "abcdefghijklmnopqrstuvwxyz"
ind = 1
for i in sample:
    chardic[i] = ind
    ind += 1
answers = []
for i in range(nq[1]):
    ques = list(map(int, input().split()))
    substr = s[ques[0]-1:ques[1]]
    outval = 0
    for i in substr:
        outval += chardic[i]
    answers.append(outval)

for i in answers:
    print(i)
