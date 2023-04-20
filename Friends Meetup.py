# cook your dish here
t = int(input())
while(t>0):
    x,y = map(int,input().split())
    if x == y:
        print("YES")
        t -= 1
        continue
    if y>x:
        print("NO")
        t -= 1
        continue
    if x>y:
        print("YES")
    t -= 1
