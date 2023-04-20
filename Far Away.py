# cook your dish here
t = int(input())
while(t>0):
    x,m = map(int,input().split())
    l = list(map(int,input().split()))
    sum = 0
    for i in l:
        if abs(i-m) > abs(i-1):
            sum += abs(i-m)
        else:
            sum += abs(i-1)
    print(sum)
    t -= 1
    
