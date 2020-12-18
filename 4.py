def diagonalglav(a):#Сумма главной диагонали
    sum=0
    for i in range(len(a)):
        sum+=a[i][i]# У элемнтов главной диагонали совпадют номер строки и номер столбца
    return sum
def diagonalpoboch(a):#Сумма побочной диагонали
    sum=0
    for i in range(len(a)):
        sum+=a[i][len(a)-1-i]# У элемнтов главной диагонали номер столбца равен размеру матрицы минус номер строки
    return sum
a=[]
n=int(input())#Ввод массива
for i in range(n):
    a.append(list(map(int,input().split())))
print(diagonalglav(a))
print(diagonalpoboch(a))