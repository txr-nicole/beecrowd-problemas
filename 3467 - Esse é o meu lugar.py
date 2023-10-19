while True:
    try:
        lugar= input().lower()
        if lugar[2] == 'l':
            print('Esse eh o meu lugar')
        else:
            print('Oi, Leonard')
    except EOFError:
        break
