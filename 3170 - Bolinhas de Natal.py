bolinhas = int(input())
galhos = int(input())
if galhos % 2 != 0:
    galhos -= 1
qtdNecessaria = galhos // 2
qtdFaltante = qtdNecessaria - bolinhas

if qtdNecessaria <= bolinhas :
    print("Amelia tem todas bolinhas!")
else:
    print(f"Faltam {qtdFaltante} bolinha(s)")
