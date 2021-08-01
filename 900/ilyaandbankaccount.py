num = input()

if(num[0] == "-"):
    if(int(num[-1]) > int(num[-2])):
        print(int(num[:-1]))
    else:
        print(int(num[:-2]+num[-1]))
else:
    print(num)
