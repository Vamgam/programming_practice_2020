a = list(map(int, input().split()))
max1=0
min1=0
for i in range(len(a)):
    if a[i]>a[max1]:
        max1=i
    if a[i]<a[min1]:
        min=i
a[max1],a[min1]=a[min1],a[max1]
print(*a)