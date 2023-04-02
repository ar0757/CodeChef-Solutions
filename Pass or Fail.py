# cook your dish here
t = int(input())
while(t>0):
    n,x,p = map(int,input().split())
    if(x*3+(n-x)*-1 >= p):
        print("PASS")
    else:
        print("FAIL")
    t -= 1
