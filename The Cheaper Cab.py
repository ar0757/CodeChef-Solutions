# cook your dish here
t = int(input())
while(t>0):
    l = list(map(int,input().split()))
    if(l[0]>l[1]):
        print("SECOND")
    elif(l[0]<l[1]):
        print("FIRST")
    else:
        print("ANY")
    t -= 1
