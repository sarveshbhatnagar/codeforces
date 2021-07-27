# A. I Wanna Be the Guy

n = int(input())
x = set(list(map(int, input().split()))[1:])
y = set(list(map(int, input().split()))[1:])
if(len(x.union(y)) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
