# cook your dish here
t = int(input())
while(t>0):
    n,x,s = map(int,input().split())
    l = []
    for i in range(n):
        l.append(0)
    l[x-1] = 1
    for i in range(s):
        a,b = map(int,input().split())
        temp = l[a-1]
        l[a-1]=l[b-1]
        l[b-1] = temp
    print(l.index(1)+1)
    t -= 1
        
