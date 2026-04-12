continuar = 1
denuncias = []

while continuar == 1:
    print('BEM VINDO AO DISK DENÚNCIA')
    print('DIGITE O NÚMERO DA SUA DENÚNCIA')
    print('1. BURACO')
    print('2. LIXO')
    print('3. ILUMINAÇÃO')

    denu = int(input('=====> '))

    if denu not in (1, 2, 3):
        print('Escolha uma das opções')
    else:
        desc = input('Digite sua denúncia: ')
        loc = input('Digite sua localização: ')
        st = 'Pendente'
        dt = '18/05/2026'

        if denu == 1:
            tipo = 'BURACO'
        elif denu == 2:
            tipo = 'LIXO'
        else:
            tipo = 'ILUMINAÇÃO'

        registro = f'Tipo: {tipo} | Descrição: {desc} | Localização: {loc} | Status: {st} | Data: {dt}'
        denuncias.append(registro)

        print('\nDENÚNCIA CADASTRADA COM SUCESSO!')
        print(registro)

    print('\nDeseja fazer outra denúncia?')
    print('1. SIM')
    print('2. NÃO')
    continuar = int(input('=====> '))

print('\n TODAS AS DENÚNCIAS REGISTRADAS:')
for denuncia in denuncias:
    print(denuncia)

print('\nSistema encerrado')