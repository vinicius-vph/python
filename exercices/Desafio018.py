#faça um prgrama que leia um angulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse angulo
print('======================================================')
print('Vamos calcular o seno, cosseno e tangente desse angulo')
print('======================================================\n')
from math import sin,cos,tan,radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('\nO angulo digitado foi {}°\nseu seno é {:.2f}\nseu cosseno {:.2f}\ne sua tangente {:.2f}.'.format(angulo,seno,cosseno,tangente))

