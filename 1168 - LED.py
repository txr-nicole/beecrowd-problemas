linha = int(input())
cont = 0
led = []
while cont < linha:
    led = list(map(int,input()))
    somaLed = 0
    for i in range(0,len(led)):
        if led[i] == 1:
            somaLed += 2
        elif led[i] == 2:
            somaLed += 5
        elif led[i] == 3:
            somaLed += 5
        elif led[i] == 4:
            somaLed += 4
        elif led[i] == 5:
            somaLed += 5
        elif led[i] == 6:
            somaLed += 6
        elif led[i] == 7:
            somaLed += 3
        elif led[i] == 8:
            somaLed += 7
        elif led[i] == 9:
            somaLed += 6
        else:
            somaLed += 6
    print(f'{somaLed} leds')
    cont += 1
