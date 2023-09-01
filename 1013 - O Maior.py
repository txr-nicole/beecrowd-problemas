valores = input().split()

n1 = int(valores[0])
n2 = int(valores[1])
n3 = int(valores[2])

maior = (n1+n2+abs(n1-n2))/2
maiorDoMaior = (maior+n3+abs(maior-n3))/2
print(f'{maiorDoMaior:.0f} eh o maior')
