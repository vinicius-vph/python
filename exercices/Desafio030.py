#Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar
print('============================================')
print('Vamos verificar se um número é par ou ímpar:')
print('============================================\n')
numero = int(input('Digite um número: '))
if (numero % 2) == 0:
	print('\n{} é um número par'.format(numero))
else:
	print('\n{} é um número ímpar'.format(numero))
