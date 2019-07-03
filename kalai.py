s1,s2=map(int,input().split())
flag=0
for i in  range(1,s1):
    if s2**i==s1:
        flag=1
        break
if flag==1:
    print("yes")
else:
    print("no")
