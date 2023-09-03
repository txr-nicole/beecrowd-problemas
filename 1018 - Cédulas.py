valor = int(input())
valorTotal = valor
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0
while valor > 0:
    if (valor >= 100):
        notas100 += 1
        valor -= 100
    elif (valor >= 50):
        notas50 += 1
        valor -= 50
    elif (valor >= 20):
        notas20 += 1
        valor -= 20
    elif (valor >= 10):
        notas10 += 1
        valor -= 10
    elif (valor >= 5):
        notas5 += 1
        valor -= 5
    elif (valor >= 2):
        notas2 += 1
        valor -= 2
    else:
        notas1 += 1
        valor -= 1
print(f'{valorTotal}\n{notas100} nota(s) de R$ 100,00\n{notas50} nota(s) de R$ 50,00\n{notas20} nota(s) de R$ 20,00\n{notas10} nota(s) de R$ 10,00\n{notas5} nota(s) de R$ 5,00\n{notas2} nota(s) de R$ 2,00\n{notas1} nota(s) de R$ 1,00')
        
