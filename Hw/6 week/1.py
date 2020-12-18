def power(a,n): #Сама функция
    if n==0:#a^0=1
        return 1
    if n>0:#a^n=a*a*...*a
        return a*power(a,n-1)
    if n<0:#a^n=1/(a*a...*a)
        return 1/(a*power(a,abs(n)-1))
print(power(2,2))