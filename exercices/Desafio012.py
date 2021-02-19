#faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print('=' * 118)
print('Toda a loja está com 5% de desconto, digite abaixo o valor do produto e veja  qual é o valor final já com o desconto!')
print('=' * 118)

a = float(input('\nDigite o valor do produto : R$ '))
vd = a*0.05
vf = a - vd
print('\nO desconto foi de R$ {:.2f}, o produto sairá por R$ {:.2f}'.format(vd, vf))
print('\nAté a próxima !')