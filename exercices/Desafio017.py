#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa.
#modo 1
print('===========================================')
print('Vamos calcular a hipotenusa de um triângulo')
print('===========================================\n')
cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('\nO valor digitado foi cateto oposto {}, cateto adjacente {}, e a hipotenusa é {}'.format(cateto_oposto,cateto_adjacente,hipotenusa))
#modo 2
from math import hypot
cateto_oposto = float(input('\nDigite um valor para o cateto oposto: '))
cateto_adjacente = float(input('\nDigite um valor para o cateto adjacente: '))
hipotenusa = hypot(cateto_oposto,cateto_adjacente)
print('\no valor digitado para cateto oposto foi {}, para cateto adjacente {}, então sua hipotenusa é {}'.format(cateto_oposto,cateto_adjacente,hipotenusa))


