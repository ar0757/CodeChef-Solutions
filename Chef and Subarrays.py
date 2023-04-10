from math import *
t = int(input())
while(t>0):
    x = int(input())
    l = list(map(int,input().split()))
    k,perm = 1,0
    m = []
    for _ in range(len(l)):
        k = 1
        k += perm
        i = 0
        while(k<=len(l)):
            m.append(l[i:k])
            k += 1
            i += 1
        perm += 1
    count = 0
    for i in m:
        if sum(i) == prod(i):
            count += 1
    print(count)
    t -= 1
    
        
