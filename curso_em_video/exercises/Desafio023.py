#faça um programa que leia um numero entre 0 e 9999, e mostre na tela cada um dos digitos
#separadores, ex: 1894 (unidade: 4, dezena 3 centena 8 milhar 1)
print('============================================================')
print('Vamos separar um número em unidade, dezena, sentena e milhar')
print('============================================================\n')
numero = int(input('Digite um número entre 0 e 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('\nAnalisando o número {}'.format(numero))
print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('A milhar é {}'.format(m))

