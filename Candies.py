# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(2*n):
        if a.count(a[i]) >= 3:
            print('No')
            break
    else:
        print('yes')
