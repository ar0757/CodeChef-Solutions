# cook your dish here
t = int(input())
while(t>0):
    x1,y1,x2,y2=map(int,input().split())
    print(max(abs(x1-x2),abs(y1-y2)))
    t -= 1
