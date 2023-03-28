# cook your dish here
t = int(input())
while(t>0):
    n,x,k=map(int,input().split())
    if k/x > n:
        print(n)
    else:
        print(int(k/x))
    t -= 1
