def F(n):
    if n>1:
        return n*F(n-1)
    else:
        return 1
m=int(input())
sum=0
for i in range(1,m+1):
    sum+=F(i)
print(sum)