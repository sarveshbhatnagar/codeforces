# 1 -> 2
# 2 -> 3
# 3 -> 4
# 4 -> 1

n = input()
gifters = list(map(int, input().split()))
myGifters = dict()
for i in range(1, len(gifters)+1):
    myGifters[gifters[i-1]] = i
answer = []
for i in range(1, len(gifters)+1):
    answer.append(str(myGifters[i]))
print(" ".join(answer))
# print(answer)
