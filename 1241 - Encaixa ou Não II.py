qtde = int(input())
cont = 0
while cont < qtde:
    cont += 1
    teste, parte = input().split()
    tamP = len(parte)
    tamT = len(teste)
    tamanhoFinal = tamT - tamP   
    corte = slice(tamanhoFinal, tamT)
    if teste[corte] == parte:
        print('encaixa')
    else:
        print('nao encaixa')
