# cook your dish here
t = int(input())
while(t>0):
    x,y,a,b = map(int,input().split())
    count = 0
    for i in [x,y]:
        if i not in [a,b]:
            count += 1
    print(count)
    t -= 1
