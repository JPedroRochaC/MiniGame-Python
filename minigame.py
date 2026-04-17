import random
jogar = 'S'
while jogar == 'S':
    print('======= ADVINHE O NÚMERO =======')
    print('Nivel de dificuldade')
    print('1. FÁCIL (10 a 20)')
    print('2. MÉDIO (10 a 30)')
    print('3. DIFÍCIL (10 a 40)')
    while True:
        entrada = input('Digite seu nível de dificuldade (1-3): ')
        if entrada.isdigit():
            dificuldade = int(entrada)
            if dificuldade in [1, 2, 3]:
                break
        print('Escolha apenas 1, 2 ou 3.')

    if dificuldade == 1:
        minimo, maximo = 10, 20
    elif dificuldade == 2:
        minimo, maximo = 10, 30
    else:
        minimo, maximo = 10, 40
    while True:
        numero = random.randint(minimo, maximo)

        P = numero % 2 == 0
        Q = numero >= 10
        R = numero % 3 == 0

        if (P and Q) and not R:
            break 

    print('\nRegras:')
    print('P: número é par')
    print('Q: número é maior ou igual a 10')
    print('R: número é múltiplo de 3')
    print('Condição: (P ∧ Q) ∧ ¬R')
   
    print('\n======= VALENDO =======')
    while True:
        entrada = input(f'Seu chute ({minimo}-{maximo}): ')
        if entrada.isdigit():
            chute = int(entrada)
            if minimo <= chute <= maximo:
                break
        print(f'Apenas número entre {minimo} e {maximo}.')
    contador = 1
    while chute != numero:
        contador += 1

        if chute > numero:
            print('Muito alto')
        else:
            print('Muito baixo')

        while True:
            entrada = input(f'Seu chute ({minimo}-{maximo}): ')
            if entrada.isdigit():
                chute = int(entrada)
                if minimo <= chute <= maximo:
                    break
            print(f'Apenas número entre {minimo} e {maximo}.')


    print(f'\nParabéns! Você acertou, o número era {numero}!')
    print(f'Tentativas: {contador}')
    print('\nValores lógicos:')
    print(f'P: VERDADEIRO | Q: VERDADEIRO | R: FALSO')
    print('\nVamos jogar novamente?')
    jogar = input('[S/N]: ').upper()
print('Até mais!')