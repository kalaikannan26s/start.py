k1,c=map(int,input().split())
l=[]
k1_ind=[]

for i in range(k1):
    l.append(list(map(int,input().split())))


for i in range(r):
    for j in range(c):
        if l[i][j]==0:
            k1_ind.append([i,j])

for i in k1_ind:
      for x in range(c):
          l[i[0]][x]=0
      for y in range(k1):
          l[y][i[1]]=0
c=c-1
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print(l[i][c])    
