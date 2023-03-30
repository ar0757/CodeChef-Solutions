# cook your dish here
t = int(input())
while(t>0):
    x,y,d = map(int,input().split())
    if(abs(x-y)<=d):
        print("YES")
    else:
        print("NO")
    t -= 1
