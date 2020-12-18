def NOD(a,b):#Тут алгоритм Евклида
    while a != 0 and b != 0:
        if a > b:
            a=a-b
        else:
            b=b- a
    return a
print(NOD(4,7))