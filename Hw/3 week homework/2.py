a=list(map(int,input().split()))
m=max(a)
m1=min(a)
i=a.index(m1)
a[a.index(m)]=m1
a[i]=m
print(*a)