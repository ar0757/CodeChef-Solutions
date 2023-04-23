# cook your dish here
t= int(input())
d={1:[10000000000],2:[1000000000000],3:[100000000000000]}
c=list(map(int, input().split()))
n=list(map(int, input().split()))
for i in range(t):
    if(n[i]==1):
        d[1].append(c[i])
    elif(n[i]==2):
        d[2].append(c[i])
    else:
        d[3].append(c[i])
print(min(min(d[1])+min(d[2]),min(d[3])))
