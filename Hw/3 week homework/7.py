a=int(input())
m=[]
for i in range(a):
    b=input().split()
    for q in b:
        if q in m!=True:
            m.append(q)
print(len(m))
