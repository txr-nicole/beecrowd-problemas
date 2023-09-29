nTrab = float(input())
nProv = float(input())
media = (nTrab + nProv) / 2
if media < 6 and nTrab >= 2:
    print('talvez com a sub')
elif media < 6 and nTrab < 2:
    print('reprovado')
else:
    print('aprovado')

