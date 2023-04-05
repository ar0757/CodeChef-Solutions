# cook your dish here
t = int(input())
while(t>0):
    x,y=map(int,input().split())
    if (x%2==0 and y%2==0) or (x%2!=0 and y%2!=0):
        print("Janmansh")
    elif (x%2==0 and y%2!=0) or (x%2!=0 and y%2==0):
        print("Jay")
    t -= 1
