count = 0
soma = 0
pos = 0
while count < 6:
    num = float(input())
    if num > 0:
        soma += num
        pos += 1
    count += 1
print(f'{pos} valores positivos\n{soma/pos:.1f}')
