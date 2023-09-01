pontos1 = input().split()
pontos2 = input().split()
x1 = float(pontos1[0])
y1 = float(pontos1[1])
x2 = float(pontos2[0])
y2 = float(pontos2[1])
distancia = ((x2 - x1)**2) +((y2 - y1)**2)
raiz = distancia**0.5
print(f'{raiz:.4f}')
