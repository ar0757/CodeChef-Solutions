# cook your dish here
a = int(input())
n = 0

while n < a:
    b = list(map(int, input().split()))
    if b[0] + b[1] <= b[3]and b[2] <= b[4]:
        print("YES")
        n += 1
        continue
    if b[1] + b[2] <= b[3]and b[0] <= b[4]:
        print("YES")
        n += 1
        continue
        
    if b[0] + b[2] <= b[3]and b[1] <= b[4]:
        print("YES")
        n += 1
        continue
    else:
        print("NO")
        n += 1
        continue
    b = []
    
