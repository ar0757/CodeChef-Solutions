# cook your dish here
t = int(input())
while(t>0):
    l = list(map(int,input().split()))
    req = l[:2]
    A = l[2:4]
    B = l[4:]
    if sorted(req)==sorted(A):
        print(1)
    elif sorted(req)==sorted(B):
        print(2)
    else:
        print(0)
    t -= 1
    
