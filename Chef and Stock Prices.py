# cook your dish here
t = int(input())
while(t>0):
    s,a,b,c= map(int,input().split())
    s = abs(s)+(s*(c/100))
    if a<=s<=b:
            print("Yes")
    else:
            print("No")
    t -= 1
