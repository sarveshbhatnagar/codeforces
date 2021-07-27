word = input()
letters = set("abcdefghijklmnopqrstuvwxyz")
small = 0
for i in word:
    if(i in letters):
        small += 1

if(len(word) - small > small):
    print(word.upper())
else:
    print(word.lower())
