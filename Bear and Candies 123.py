# cook your dish here
t = int(input())
while(t>0):
    x,y=map(int,input().split())
    count = 1
    flag =0
    while(True):
        if flag == 0:
            if x>= count:
                x -= count
                count += 1
                flag = 1
            else:
                print("Bob")
                break
        else:
            if y>= count:
                y -= count
                count += 1
                flag = 0
            else:
                print("Limak")
                break
    t -= 1
