nome = input()
salario = float(input())
vendas = float(input())
comissao = vendas * 0.15
total_mes = salario + comissao
print(f'TOTAL = R$ {total_mes:.2f}')
