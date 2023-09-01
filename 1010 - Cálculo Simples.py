peca1 = input().split()
peca2 = input().split()
subtotal1 = int(peca1[1]) * float(peca1[2])
subtotal2 = int(peca2[1]) * float(peca2[2])
total = subtotal1 + subtotal2
print(f'VALOR A PAGAR: R$ {total:.2f}')
