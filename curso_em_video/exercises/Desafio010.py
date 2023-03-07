#crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dolares ela pode comprar considerando U$$1/R$6,46
print('=' * 46)
print('Vamos mostrar o quão pobre você é em dólares!')
print('=' * 46)

a = float(input('\nDiga-me quantos (R$) reais você tem na carteira e eu te digo quantos dólares você pode comprar. \n\nQuantos reais você tem? R$ '))
print('\nCom R$ {:.2f} você pode comprar U$$ {:.2f} dólares'.format(a, a / 5.46))
print('\nAté a próxima !')
