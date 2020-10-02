a=list(map(int,input().split()))
k=0
for i in range(1,len(a)-1):
    if a[i]>(a[i-1]+a[i+1])/2:
        k+=1
print(k)
