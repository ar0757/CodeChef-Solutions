# cook your dish here
t = int(input())
while(t>0):
    x,y = map(int,input().split())
    sum = 0
    count = 0
    while(sum != x):
        if sum+y>x:
            sum += 1
        else:
            sum += y
        count += 1
    print(count)
    t -= 1
