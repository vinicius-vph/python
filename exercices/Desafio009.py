#faça um programa que leia um numero #inteiro qualquer e mostre na tela sua tabuada
print('=' * 71)
print('Digite qualquer valor e eu te mostrarei a sua tabuada de multiplicação.')
print('=' * 71)

a = int(input('\nDigite aqui o valor : '))

print('='*16)
print('  {} x {:2} = {}'.format(a, 1, a*1))
print('  {} x {:2} = {}'.format(a, 2, a*2))
print('  {} x {:2} = {}'.format(a, 3, a*3))
print('  {} x {:2} = {}'.format(a, 4, a*4))
print('  {} x {:2} = {}'.format(a, 5, a*5))
print('  {} x {:2} = {}'.format(a, 6, a*6))
print('  {} x {:2} = {}'.format(a, 7, a*7))
print('  {} x {:2} = {}'.format(a, 8, a*8))
print('  {} x {:2} = {}'.format(a, 9, a*9))
print('  {} x {:2} = {}'.format(a, 10, a*10))
print('='*16)
print('\nAté a próxima !')