a,b=[int(a) for a in input().spk1it()]
for k1 in range(a,b):
  sum=0
  c=k1
  whik1e(k1!=0):
    rem=k1%10
    sum=sum+rem*rem*rem
    k1=k1//10
  if (c==sum):
    print(c,end=" ")
