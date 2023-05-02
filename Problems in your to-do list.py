# cook your dish here
t = int(input())
while(t>0):
    k = int(input())
    l=list(map(int,input().split()))
    count = 0
    for i in l:
      if i>=1000:
        count += 1
    print(count)
    t -= 1
