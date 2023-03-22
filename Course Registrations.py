# cook your dish here
t = int(input())
while(t>0):
    x,y,z=map(int,input().split())
    if((y-z)>=x):
        print("Yes")
    else:
        print("No")
    t -= 1
    
