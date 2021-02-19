#crie um programa que leia um numero real qualquer pela teclado e mostre na tela a sua porção inteira
#ex digit 6.127 e apareça 6
print('=' * 50)
print('Digite um número decimal e eu te digo a parte inteira')
print('=' * 50)
#modo 1
num = float(input('\nDigite um número decimal : '))
print('\nO número digitado foi {} e sua parte inteira é {}'.format(num,int(num)))
#modo 2
from math import trunc
num = float(input('\nDigite um número decimal e eu te digo a parte inteira: '))
print('\nO número digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))

