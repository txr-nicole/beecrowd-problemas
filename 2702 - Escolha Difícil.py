disp = list(map(int,input().split()))
req = list(map(int, input().split()))
soma = 0
for i in range(0,3):
    if disp[i]-req[i] < 0:
        soma = soma + (disp[i]-req[i])
print(abs(soma))
    
