dSemana = input()
dias = int(input())
hoje = 0
if dSemana == 'segunda':
    hoje = 1
elif dSemana == 'terca':
    hoje = 2
elif dSemana == 'quarta':
    hoje = 3
elif dSemana == 'quinta':
    hoje = 4
elif dSemana == 'sexta':
    hoje = 5
elif dSemana == 'sabado':
    hoje = 6
else:
    hoje = 0


if dias == 0:
    print('chega hoje!')
else:
    if hoje + dias == 1 or hoje + dias == 8:
        print('sera entregue segunda')
    elif hoje + dias == 2 or hoje + dias == 9:
        print('sera entregue terca')
    elif hoje + dias == 3 or hoje + dias == 10:
        print('sera entregue quarta')
    elif hoje + dias == 4 or hoje + dias == 11:
        print('sera entregue quinta')
    elif hoje + dias == 5 or hoje + dias == 12:
        print('sera entregue sexta')
    elif hoje + dias == 6 or hoje + dias == 13:
        print('sera entregue sabado')
    else:
        print('sera entregue domingo')
