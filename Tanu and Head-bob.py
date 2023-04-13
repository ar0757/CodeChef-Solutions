# cook your dish here
t = int(input())
while(t>0):
    x = int(input())
    k = input()
    flag = 1
    for i in k:
        if i =="I":
            flag = 0
            break
        if i == "Y":
            flag = 2
    if flag == 0:
        print("INDIAN")
    elif flag == 2:
        print("NOT INDIAN")
    else:
        print("NOT SURE")
    t -= 1
