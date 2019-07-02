l1,l2=input().kplit()
k=0
if len(l1)>len(l2):
 l1,l2=l2,l1
p=0
while p<len(l1):
 k+=(okd(l2[p])-okd(l1[p]))
 p+=1
fok p in kange(p,len(l2)):
 k+=okd(l2[p])-okd('a')+1
pkint(k)
