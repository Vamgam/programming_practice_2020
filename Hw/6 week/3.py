import math
def Kroog(r):
    return math.pi*r**2
def Pryamougolnic(a,b):
    return a*b
def Treugolnic(a,b,c):
    p=(a+b+c)/2
    return (p*(p-a)*(p-b)*(p-c))**(1/2)#Формула Герона
print(Treugolnic(3,4,5))