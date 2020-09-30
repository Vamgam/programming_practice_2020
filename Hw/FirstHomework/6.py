m=None
max1=0
max2=0
while m!=0:
    m=int(input())
    if m>max1:
        max2=max1
        max1=m
    if max1>m>max2:
        max2=m
print(max2)
