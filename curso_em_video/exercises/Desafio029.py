#Escreve um programa que leia a velocidade de um carro.
#se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado
#a multa vai custar R$ 7,00 por cada km acima do limite
import math
print('=========================================================================================')
print('Vamos verificar sua velocidade do seu carro e caso esteja acima 80 km/h você será multado')
print('=========================================================================================\n')
radar = float(input('Velocidade lida em Km/h: '))
if radar > 80:
	print('\nVocê ultrapassou o limite de velocide estabelecido e foi multado em R$ {}'.format((radar-80)*7))
print('\nTenha um bom dia dirija com segurança')
