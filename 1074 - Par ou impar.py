num = int(input())
count = 0
while count < num:
    valor = int(input())
    count += 1
    if valor == 0:
        print('NULL')
    else:
        if valor > 0 and valor % 2 == 0: print('EVEN POSITIVE')
        elif valor > 0 and valor % 2 != 0: print('ODD POSITIVE')
        elif valor < 0 and valor % 2 == 0: print('EVEN NEGATIVE')
        else: print('ODD NEGATIVE')
