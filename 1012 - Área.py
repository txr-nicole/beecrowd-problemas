area = input().split()
A = float(area[0])
B = float(area[1])
C = float(area[2])


print(f'TRIANGULO: {A*C/2:.3f}\nCIRCULO: {3.14159*C**2:.3f}\nTRAPEZIO: {(A+B)*C/2:.3f}\nQUADRADO: {B**2:.3f}\nRETANGULO: {A*B:.3f}')

