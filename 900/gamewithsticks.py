nk = list(map(int, input().split()))

lastplay = False

n, k = nk[0], nk[1]

while(n >= 1 and k >= 1):
    lastplay = not lastplay
    n -= 1
    k -= 1

if(lastplay):
    print("Akshat")
else:
    print("Malvika")
