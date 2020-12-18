a = list(map(int, input().split()))
m=0
for i in range(len(a)):
    for k in range(i+1,len(a)):
        if a[i]==a[k]:
            m += 1
print(m)