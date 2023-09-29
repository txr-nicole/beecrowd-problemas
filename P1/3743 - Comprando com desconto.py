valor = float(input())
qtde = int(input())
semDesc = valor * qtde
desc = valor * (0.1 + (qtde/100))
totalComDesc = semDesc - (desc * qtde)
print(f'{semDesc:.2f}\n{totalComDesc:.2f}')
