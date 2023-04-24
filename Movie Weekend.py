# cook your dish here
t = int(input())
while(t>0):
    x = int(input())
    l = list(map(int,input().split()))
    m = list(map(int,input().split()))
    max = l[0]*m[0]
    index = 0
    MofI = m[0]
    for i in range(1,len(l)):
        if l[i]*m[i] > max:
            max = l[i]*m[i]
            index = i
            MofI = m[i]
        elif l[i]*m[i] == max and m[i] > MofI:
            max = l[i]*m[i]
            index = i
            MofI = m[i]
    print(index+1)
    t -= 1
