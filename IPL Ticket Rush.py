# cook your dish here
t = int(input())
while(t):
    x,y = map(int,input().split())
    if y>=x:
        print(0)
    else:
        print(x-y)
    t -= 1
