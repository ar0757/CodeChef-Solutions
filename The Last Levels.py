# cook your dish here
t = int(input())
while(t>0):
    count = 0
    sum = 0
    lvl,time,off=map(int,input().split())
    for i in range(lvl):
        if count<3 :
            count += 1
            sum += time
        if count == 3 and i!=lvl-1:
            sum += off
            count = 0
    print(sum)
    t -= 1
