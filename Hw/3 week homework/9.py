a=dict()
m=dict()
b=input().split()
while len(b[0])!=0:
    k =b[0]
    if k in a:
            a[k].append(b[1])
            m[k].append(b[2])
    else:
            a[k]=[b[1]]
            m[k]=[b[2]]
    a[k]=sorted(a[k])
    b = input().split()
for k in a:
    print(k,':')
    for b in a[k]:
        print(*b)
