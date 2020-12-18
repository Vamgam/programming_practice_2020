n = int(input())
s = set()
for i in range(n):
    row = input().split()
    s.update(row)
s = sorted(s)
b=[s.count(i) for i in s]
print(s[b.index(max(b))])

