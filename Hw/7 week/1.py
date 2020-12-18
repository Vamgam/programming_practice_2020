a = list(map(int, input().split()))
c=0
for i in range(1,len(a)-1):
    if a[i]>(a[i-1]+a[i+1])/2: #Если а>b и a>c, то 2a>(b+c)
        c+=1
print(c)