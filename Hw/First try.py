def F(n):
    if n>1:
      return "Hello\n"+F(n-1)
    else:
        return "Hello"
print(F(5))