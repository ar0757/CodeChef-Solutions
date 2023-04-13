# cook your dish here
t = int(input())
while(t>0):
    n,v1,v2 = map(int,input().split())
    if (n*v2 < n*(2**0.5)*v1):
        print("Stairs")
    else:
        print("Elevator")
    t -= 1
