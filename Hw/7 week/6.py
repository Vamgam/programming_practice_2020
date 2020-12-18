a=input().split()
b=[]
for i in a:
    if i in b:
        print("Yes")
    else:
        print("No")
        b.append(i)
