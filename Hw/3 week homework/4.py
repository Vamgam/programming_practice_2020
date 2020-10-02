a=list(map(int,input().split()))
b=[0]*(max(a)+1)
for i in a:
    b[i]+=1
sum1=0
m=[]
for i in range(len(b)):
      if b[i]==1:
          m.append(a.index(i))
m.sort()
print(*list(a[i] for i in m))

