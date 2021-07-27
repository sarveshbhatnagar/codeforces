n = int(input())
s = input()
count_a = 0
count_b = 0
for i in s:
    if(i == "A"):
        count_a += 1
    else:
        count_b += 1

if(count_a == count_b):
    print("Friendship")
elif(count_a > count_b):
    print("Anton")
else:
    print("Danik")
