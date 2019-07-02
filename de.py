n,n1=input().split()
v1=abs(len(n)-len(n1))
for i in range(len(n)):
  if len(n1)==1 and n1[i] in n:
   break
  if n[i]!=n1[i]:
   v1+=1
print(v1)
