# cook your dish here
t = int(input())
while(t>0):
    x = int(input())
    if x%4==0:
        string = ""
        shift = 0
        for i in range(int(x/2)):
            if shift == 0:
                string += '10'
                shift = 1
            else:
                string += '01'
                shift = 0
        print(string)
    else:
        string = "10"
        for _ in range(3,x):
            string += '0'
        string += '1'
        print(string)
    t -= 1
