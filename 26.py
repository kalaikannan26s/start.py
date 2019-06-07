r1=int(input())
b=list(input().split())
b11=0
for i in range(r1):
    if(int(b[i])>0):
        a=sorted(b)
        b11=1
    else:
        c=reversed(b)
if(b11==1):
    print(' '.join(a))
else:
    print(' '.join(c))
