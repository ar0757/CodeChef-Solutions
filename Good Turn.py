# cook your dish here
t = int(input())
while(t):
    x,y = map(int,input().split())
    if (x+y>6):
        print("YES")
    else:
        print("NO")
    t -= 1
