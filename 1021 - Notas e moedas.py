valor = float(input())
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
moedas1 = 0
moedas050 = 0
moedas025 = 0
moedas010 = 0
moedas005 = 0
moedas001 = 0
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
    elif (valor >= 1):
        moedas1 += 1
        valor -= 1
    elif (valor >= 0.50):
        moedas050 += 1
        valor -= 0.50
    elif (valor >= 0.25):
        moedas025 += 1
        valor -= 0.25
    elif (valor >= 0.10):
        moedas010 += 1
        valor -= 0.10
    elif (valor >= 0.05):
        moedas005 += 1
        valor -= 0.05
    elif (valor >= 0.01):
        moedas001 += 1
        valor -= 0.01
    elif (valor >= 0.009):
        moedas001 += 1
        valor -= 0.01
    else:
        break
print(f'''NOTAS:
{notas100} nota(s) de R$ 100.00
{notas50} nota(s) de R$ 50.00
{notas20} nota(s) de R$ 20.00
{notas10} nota(s) de R$ 10.00
{notas5} nota(s) de R$ 5.00
{notas2} nota(s) de R$ 2.00
MOEDAS:
{moedas1} moeda(s) de R$ 1.00
{moedas050} moeda(s) de R$ 0.50
{moedas025} moeda(s) de R$ 0.25
{moedas010} moeda(s) de R$ 0.10
{moedas005} moeda(s) de R$ 0.05
{moedas001} moeda(s) de R$ 0.01''')

        
