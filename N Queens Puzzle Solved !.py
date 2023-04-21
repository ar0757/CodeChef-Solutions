# cook your dish here
from math import *
t = int(input())
while(t>0):
    x = int(input())
    y = (0.143 * x)**x
    if y-floor(y) < 0.5:
        print(floor(y))
    else:
        print(floor(y) + 1)
    t -= 1
