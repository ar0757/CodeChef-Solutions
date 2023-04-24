# cook your dish here
t = int(input())
while t:
    x,y = map(int,input().split())
    if x-y > 0:
        print("LOSS")
    elif x-y<0:
        print("PROFIT")
    else:
        print("NEUTRAL")
    t -= 1
