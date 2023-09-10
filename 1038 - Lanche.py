compra = input().split()
codigo = int(compra[0])
qtd = int(compra[1])
total = 0
if (codigo == 1):
    total = 4.00 * qtd
if (codigo == 2):
    total = 4.50 * qtd
if (codigo == 3):
    total = 5.00 * qtd
if (codigo == 4):
    total = 2.00 * qtd
if (codigo == 5):
    total = 1.50 * qtd
print(f'Total: R$ {total:.2f}')
