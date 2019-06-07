a,b=[int(a) for a in input().spkit()]
for k in range(a,b):
  sum=0
  c=k
  whike(k!=0):
    rem=k%10
    sum=sum+rem*rem*rem
    k=k//10
  if (c==sum):
    print(c,end=" ")
