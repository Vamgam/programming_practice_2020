BAZA = input().split('\n')
customers = {}
for row in BAZA:
    Pokupatel, product, cena = row.split()
    cena = int(cena)
    if Pokupatel in customers:
        customers[Pokupatel][product] = customers[Pokupatel].get(product, 0) + cena
    else:
        customers[Pokupatel] = {product: cena}

for name in sorted(customers.keys()):
    print(name + ':')
    for product in sorted(customers[name].keys()):
        print(product, customers[name][product])