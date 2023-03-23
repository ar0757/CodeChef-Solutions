# cook your dish here
t = int(input())
l = list(map(int,input().split()))
counto = 0
counte = 0
for i in l:
    if i%2 == 0:
        counte += 1
    else:
        counto += 1
if counto >= counte:
    print("NOT READY")
else:
    print("READY FOR BATTLE")
    
