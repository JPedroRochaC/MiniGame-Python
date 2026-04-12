1° DESAFIO
nome=str(input('Digite seu nome: '))
print(f'Seu nome em maiusculo é: {nome.upper()}')
print(f'Seu nome em minusculo é: {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(' ')} letras')
print(f'Seu primeiro nome tem {nome.find(' ')}')

2° DESAFIO
n=int(input('Digite seu número: '))
u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10
print (f'Unidades: {(u)}')
print (f'Dezenas: {(d)}')
print (f'Centenas: {(c)}')
print (f'Milhar: {(m)}')

3° DESAFIO
import random
denu=str(input('Digite sua denúncia: '))
palavras = denu.split()
if len(palavras) < 3:
    print('Denúncia inválida')
else:
 print(denu.split())
 print(palavras[0])
 print(palavras[-1])
 print(denu.upper())
 print(f"quantidade de letras: {len(denu)-denu.count(' ')}")
 print(f"quantidade de letra A: {denu.count('a')}")
 print(denu.strip().find('buraco'))
 print(denu.lower().startswith('buraco'))
 lista=['denúncia registrada', 'chamado enviado', 'problema salvo']

 print(random.choice(lista))

4° DESAFIO 
nome=str(input('Digite seu nome: ')).strip()
nomes=nome.split()
print(nomes[0])
print(nomes[-1])

