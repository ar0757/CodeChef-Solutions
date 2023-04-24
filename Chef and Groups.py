# cook your dish here
t = int(input())
while(t>0):
    x = input()
    count = 0
    zamn = 0
    for i in x:
        if i == '1':
            if zamn == 0:
                count += 1
                zamn = 1
        else:
            zamn = 0
    print(count)
    t -= 1
