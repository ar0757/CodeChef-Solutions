# cook your dish here
t = int(input())
while(t>0):
    n,a,b,c = map(int,input().split())
    if a+c >= n and b >= n :
        print("YES")
    else:
        print("NO")
    t -= 1
    
