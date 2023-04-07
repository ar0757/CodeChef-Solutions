# cook your dish here
dict = {0 : 6, 1 : 2, 2 : 5, 3 : 5, 4 :4, 5: 5,6 : 6, 7: 3, 8: 7,9 : 6}
t = int(input())
while(t>0):
    l=list(map(int,input().split()))
    r = l[0]+l[1]
    sum = 0
    for i in str(r):
        sum += dict[int(i)]
    print(sum)
    t -= 1
        
