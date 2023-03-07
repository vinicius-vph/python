#Faça um programa que leia um ano qualquer e mostre se ele é bissexto 
from datetime import date # melhoria no código realizada pelo professor
print('=========================================')
print('Digite o ano e descubra se ele é bissexto')
print('=========================================\n')
ano = int(input('Digite o ano : '))
if ano == 0:
    	ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('\nO ano de {} É ano bissexto!'.format(ano))
else:
	print('\nO ano de {} Não é ano bissexto!'.format(ano))