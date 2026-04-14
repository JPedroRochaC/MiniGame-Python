import random

jogar = 'S'

while jogar == 'S':
    print('======= ADVINHE O NÚMERO =======')
    print('Nivel de dificuldade')
    print('1. FÁCIL (1 a 10)')
    print('2. MÉDIO (1 a 15)')
    print('3. DIFÍCIL (1 a 20)')

    dificuldade = int(input('Digite seu nível de dificuldade: '))

    if dificuldade == 1:
        numero = random.randint(1, 10)
    elif dificuldade == 2:
        numero = random.randint(1, 15)
    else:
        numero = random.randint(1, 20)

    print('======= VALENDO =======')
    chute = int(input('Seu chute: '))
    contador = 1

    while chute != numero:
        contador += 1
        if chute > numero:
            print('Muito alto')
        else:
            print('Muito baixo')

        chute = int(input('Seu chute: '))

    print(f'Parabéns! Você acertou, o número era {numero}!')
    print(f'Tentativas: {contador}')

    print('Vamos jogar novamente?')
    jogar = input('[S/N]: ').upper()
print('Até mais!')