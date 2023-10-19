inicio, fim = list(map(int,input().split()))
if inicio > fim or inicio == fim:
    duracao = (24 - inicio) + fim
else:
    duracao = fim - inicio
print(f'O JOGO DUROU {duracao} HORA(S)')
