import string
t = int(input())
while(t>0):
    x = int(input())
    l = input()
    flag = 1
    count = 0
    for i in l:
        if i.lower() in set(string.ascii_lowercase)-{'a','e','i','o','u'}:
            count += 1
        else:
            count =0
        if count == 4:
            flag = 0
            break
    if flag == 1:
        print("YES")
    else:
        print("NO")
    t -= 1
