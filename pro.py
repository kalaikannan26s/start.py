n11=int(input())
g11=[]
for k in range(0,n11):  
    d=input()
    g11.append(d)
list=[]
for k in zip(*g11):
    if (k.count(k[0])==len(k)): 
        list.append(k[0])
    else:
        break
print(''.join(list))
