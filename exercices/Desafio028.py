#Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça o usuario para tentar descobrir qual foi o numero escolhido pelo computador
#O programa devera escrever na tela se o usuario venceu ou perdeu

# minha resolução
from random import uniform

print('### Vamos jogar um jogo     ### \n### vou pensar em um numero ### \n### inteiro entre 0 e 5     ### \n### veja se vc consegue     ###\n### adivinhar e eu te dou   ###\n### uma mensagem personalizada!###')
numero_sorteado = int(uniform(0,5))
numero = int(input('\nO número é... '))
if numero == numero_sorteado:
	print('\nParabéns você é bom nisso o número que pensei foi {}!'.format(numero_sorteado))
else:
	print('\nHahahaha não foi dessa vez!!, o número certo era {}'.format(numero_sorteado))

#resolução do professor
from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta advinhar
print('Processando...')
sleep(3)
if jogador == computador:
    	print('Parabéns! Você conseguiu me vencer')
else:
    	print('Ganhei! Eu pensei no número {} e não no número {}'.format(computador, jogador))
    			
