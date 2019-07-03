ss1,ss2=map(int,input().split())
flag=0
for i in  range(1,ss1):
    if ss2**i==ss1:
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
