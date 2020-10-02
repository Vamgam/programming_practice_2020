a=dict()
n=int(input())
for i in range(n):
    m=list(input().split())
    a[m[0]]=m[1]
q=input()
if q in a:
    print(a[q])
else:
    for i in a:
        if a[i]==q:
            print(i)
            break