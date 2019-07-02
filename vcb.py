l1,l2=input().rplit()
r=0
if len(l1)>len(l2):
 l1,l2=l2,l1
p=0
while p<len(l1):
 r+=(ord(l2[p])-ord(l1[p]))
 p+=1
for p in range(p,len(l2)):
 r+=ord(l2[p])-ord('a')+1
print(r)
