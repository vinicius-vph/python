# crie um algoritimo que leia um numero  e mostre o seu dobro triplo e raiz quadrada
print('=' * 82)
print('Digite um número inteiro, e eu mostro o seu dobro, triplo e a sua raiz quadrada !')
print('=' * 82)
print('\nDesafio 006 resolução 1')
n1 = int(input('\nDigite aqui : '))
d = n1 * 2
t = n1 * 3
r = n1 ** 0.5
print('\nO valor digitado foi {}, seu dobro é {}, seu triplo é {}, e sua raiz quadrada {:.2f}'.format(n1, d, t, r))

print('\nDesafio 006 resolução 2')
print('\nO valor digitado foi {}, seu dobro é {}, seu triplo é {}, e sua raiz quadrada {:.2f}'.format(n1, n1*2, n1*3, n1**0.5))

print('\nDesafio 006 resolução 3')
print('\nO valor digitado foi {}, seu dobro é {}, seu triplo é {}, e sua raiz quadrada {:.2f}'.format(n1, n1*2, n1*3, pow(n1, 0.5)))
print('\nAté a próxima !')
