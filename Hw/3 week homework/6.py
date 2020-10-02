a=list(map(int,input().split()))
for i in range(len(a)):
    if a[i] in a[:i] and i>0:
        print("YES")
    else:
        print("NO")