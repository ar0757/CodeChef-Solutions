# cook your dish here
n=int(input())
a,b,c=0,0,0
for i in range(n):
    s,t=map(int,input().split())
    a+=s
    b+=t
    d=a-b
    if d>c and d>0:
        c=d
        w=1
    elif d<0 and abs(d)>c:
        c=abs(d)
        w=2
print(w,c)
    
