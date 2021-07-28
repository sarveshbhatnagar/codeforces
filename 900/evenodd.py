# https://codeforces.com/problemset/problem/318/A
nk = list(map(int, input().split()))

# Naive method
# nos = [i for i in range(1, nk[0]+1, 2)] + \
#     [i for i in range(1, nk[0]+1) if i % 2 == 0]

# print(nos[nk[1]-1])


# Better method

# 10
# 1,3,5,7,9,2,4,6,8,10

# 5o 5e
# 1+0,2+1,3+2,4+3,5+4,6-4,7-3,8-2,9-1,10-0


# 6-(10-6)
# 7-(10-7)
# 8-(10-8)
# 9-(10-9)
# 10-(10-10)


def odd(ind):
    # n+(n-1)
    return ind+(ind-1)


def even(ind, lenoflist, og=True):
    # n-(len-n) for equal part
    # n-(len-n+1) for unequal part
    if(og):
        return ind-(lenoflist-ind)
    else:
        return ind-(lenoflist-ind+1)


evenPart = nk[0]//2
oddPart = nk[0]-evenPart

# 1+0,2+1,3+2,4+3,5-(7-5),6-(7-6),7-(7-7)
# 1,3,5,7,2,4,6
# 1+0,2+1,3+2,4+3,5-(7-5+1),6-(7-6+1),7-(7-7+1)

if(nk[1] <= oddPart):
    print(odd(nk[1]))
else:
    if(oddPart == evenPart):
        print(even(nk[1], nk[0]))
    else:
        print(even(nk[1], nk[0], False))
