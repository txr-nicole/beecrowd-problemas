qtd = int(input())
cont=0
gastos = int()
verba = int()
while cont < qtd:
    t,c= input().split()
    c = int(c)

    if t == 'G':
        gastos = gastos + c

    if t == 'V':
        verba = verba + c
    cont+=1

if gastos < verba:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
