a=list(map(int,input().split()))
b=[0]*(max(a)+1)
for i in a:
    b[i]+=1
sum1=0
for i in b:
      sum1+=i*(i-1)//2
print(sum1)