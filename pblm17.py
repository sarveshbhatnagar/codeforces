dateStr = input()
answer = 0
for i in range(int(dateStr)+1, 9999):
    if (len(set(str(i))) == 4):
        answer = i
        break

print(answer)
