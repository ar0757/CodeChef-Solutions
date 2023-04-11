# cook your dish here
t = int(input())
while(t>0):
    w1,w2,x1,x2,m =map(int,input().split())
    inc = w2 - w1
    min = x1 * m
    max = x2 * m
    if inc in range(min,max+1):
        print(1)
    else:
        print(0)
    t -= 1
