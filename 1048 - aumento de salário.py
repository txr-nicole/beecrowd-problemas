sAtual = float(input())
if sAtual >= 0 and sAtual <= 400:
    desc = sAtual * 0.15
    print(f'Novo salario: {sAtual+desc:.2f}\nReajuste ganho: {desc:.2f}\nEm percentual: 15 %')
elif sAtual >= 400.01 and sAtual <= 800.00:
    desc = sAtual * 0.12
    print(f'Novo salario: {sAtual+desc:.2f}\nReajuste ganho: {desc:.2f}\nEm percentual: 12 %')
elif sAtual >= 800.01 and sAtual <= 1200.00:
    desc = sAtual * 0.10
    print(f'Novo salario: {sAtual+desc:.2f}\nReajuste ganho: {desc:.2f}\nEm percentual: 10 %')
elif sAtual >= 1200.01 and sAtual <= 2000.00:
    desc = sAtual * 0.07
    print(f'Novo salario: {sAtual+desc:.2f}\nReajuste ganho: {desc:.2f}\nEm percentual: 7 %')
else:
    desc = sAtual * 0.04
    print(f'Novo salario: {sAtual+desc:.2f}\nReajuste ganho: {desc:.2f}\nEm percentual: 4 %')


