# cook your dish here
t = int(input())
while(t>0):
    x = int(input())
    l = list(map(int,input().split()))
    m = list(map(int,input().split()))
    count = 0
    for i in range(x):
        if l[i]==m[i]:
            count += 1
    print(count)
    t -= 1
