while True:
    try:
            sent = input()
            letras = [*sent]
            ultimaLetra = ""
            for i in range(0, len(letras)):
                if letras[i] == " ":
                    letras[i] == " "
                else:
                    if ultimaLetra == ultimaLetra.upper() and ultimaLetra != "":
                        letras[i] = letras[i].lower()
                        ultimaLetra = letras[i]
                    else:
                        letras[i] = letras[i].upper()
                        ultimaLetra = letras[i]
            print("".join(letras))
    except EOFError:
        break
