notas = input().split()
N1 = float(notas[0])
N2 = float(notas[1])
N3 = float(notas[2])
N4 = float(notas[3])
media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10
if(media >= 7.0):
    print(f'Media: {media:.1f}\nAluno aprovado.')
if (media < 5.0):
    print(f'Media: {media:.1f}\nAluno reprovado.')
if(media >= 5.0 and media <= 6.9):
    print(f'Media: {media:.1f}\nAluno em exame.')
    exame = float(input())
    print(f"Nota do exame: {exame}")
    mediaPosExam = (media + exame) / 2
    if(mediaPosExam >= 5.0):
        print(f'Aluno aprovado.\nMedia final:{mediaPosExam:.1f}')
    else:
        print('Aluno reprovado.\nMedia final:{mediaPosExam:.1f}')
    
