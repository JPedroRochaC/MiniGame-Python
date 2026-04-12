DESAFIO 1
import random
numero=random.randint(1, 5)
n=int(input('Que número você acha que é de 1 a 5? \n '))
if n==numero:
    print('Você GANHOU')
else :
    print('Você PERDEU')
print('=======')
print(f'O número era {numero} ')

DESAFIO 2
vel=int(input('Digite sua velocidade: '))
multa = vel - 80
if vel <= 80:
    print('Liberado')
else: 
    print(f'Multa de R${multa*7}')
  
DESAFIO 3 
km=int(input('Quantos km é a sua viagem? '))
preco1= km*0.50
preco2= km*0.45

if km <= 200:
    print(f'O valor da sua passagem é de R${preco1:.1f}')
else: 
    print(f'O valor da sua passagem é de R${preco2:.1f}')

DESAFIO 4 
ano=int(input('Vamos saber se seu ano é bissexto, digite aqui: '))
if ano % 4 == 0:
    print('Seu ano é bissexto')
else: 
    print('Seu ano não é bissexto')

DESAFIO 5 
sala=int(input('Digite seu salário: '))
aum1=sala*0.10
aum2=sala*0.15
if sala >= 1250:
    print(f'Seu salário teve aumento de R${aum1:.2f} e agora é R${sala+aum1:.2f}')
else:
    print(f'Seu salário teve aumento de R${aum2:.2f} e agora é R${sala+aum2:.2f}')

DESAFIO 6 
c1=int(input('Digite aqui o primeiro comprimento do triângulo: '))
c2=int(input('Digite aqui o segundo comprimento do triângulo: '))
c3=int(input('Digite aqui o terceiro comprimento do triângulo: '))
if c1+c2 > c3 and c1+c3 > c2 and c2+c3 > c1 :
    print('É possível sim formar um triângulo')
else:
    print('Não é possível formar um triângulo')