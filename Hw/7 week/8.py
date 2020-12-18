a = {}
n = int(input())
for i in range(n):
    word, synonym = input().split()
    a[word] = synonym
    a[synonym] = word
goal_word = input()
print(a[goal_word])