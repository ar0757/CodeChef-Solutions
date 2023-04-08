# cook your dish here
t = int(input())
while(t>0):
    x,b = map(int,input().split())
    l = []
    for _ in range(x):
        l.append(list(map(int,input().split())))
    k = 0
    max = 0
    for i in range(len(l)):
        if l[i][2]<=b and l[i][0]*l[i][1] > max:
            max = l[i][0]*l[i][1]
    if max == 0:
        print("no tablet")
    else:
        print(max)
    t -= 1
    
