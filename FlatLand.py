# cook your dish here
from math import  *
t = int(input())
while(t>0):
    x = int(input())
    y = x ** 0.5
    y = floor(y)
    count = 0
    while(y):
        count += 1
        x -= y ** 2
        y = x ** 0.5
        y = floor(y)
    print(count)
    t -= 1
    
    
