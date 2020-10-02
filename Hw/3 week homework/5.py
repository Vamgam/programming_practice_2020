a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=min(min(a),min(b))
mx=max(max(a),max(b))
for i in range(m,mx+1):
    if (i in a) and (i in b):
        print(i,end=' ')