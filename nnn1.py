k1,k2=input().split()
t=abs(len(k1)-len(k2))
for v in range(len(k1)):
    if len(k2)==1 and k2[v] in k1:
        break
    if k1[v]!=k2[v]:
        t+=1
print(t)
