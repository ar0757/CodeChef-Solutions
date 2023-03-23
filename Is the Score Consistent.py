# cook your dish here
t = int(input())
while(t>0):
    l = list(map(int,input().split()))
    k = list(map(int,input().split()))
    flag = 1
    for i in range(2):
        if k[i]>=l[i]:
            pass
        else:
            flag = 0
            break
    if(flag == 1):
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
    t -= 1
