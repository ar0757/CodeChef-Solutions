# cook your dish here
t = int(input())
while(t>0):
    l = list(map(int,input().split()))
    l.remove(max(l))
    print(max(l))
    t -= 1
    
