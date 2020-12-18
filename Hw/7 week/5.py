a = list(map(int, input().split()))
b=list(map(int,input().split()))
c=[i for i in a if  i in b]
print(*sorted(c))