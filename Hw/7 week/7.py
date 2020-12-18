n = int(input())
s = set()
for i in range(n):
    row = input().split()
    s.update(row)
print(len(s))