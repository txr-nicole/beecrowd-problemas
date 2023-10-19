casos = int(input())
count = 0
while count < casos:
    qtd = float(input())
    dias = 0
    while qtd > 1:
        qtd /= 2
        dias += 1
    print(f"{dias} dias")
    count += 1
