S, B, C = map(int, input().split())
tempo_SBC = 1 / (1/S + 1/B + 1/C)
print(f'{tempo_SBC:.3f}')
