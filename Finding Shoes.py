# cook your dish here
t = int(input())
while(t>0):
    n,m = map(int,input().split())
    if m>=n:
        print(n)
    elif n>m and m!=0:
        print(m +(n-m)*2)
    else:
        print(n*2)
    t -= 1
    
