#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a
# quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2 metros quadrados
print('=' * 120)
print('Vamos calcular quantos litros de tinta são necessários para pintar a parede da sua casa, Cada litro de tinta cobre 2 m2 ')
print('=' * 120)

a = float(input('\nDigite a altura da parede em metros : '))
l = float(input('\nDigite a largura da parede em metros : '))
ar = a * l
li = ar / 2
print('\nSua parede tem {:.2f} x {:.2f} metros, que dá uma área de {:.2f} m², Você precisa de {:.0f} litros de tinta para pintar sua parede.'.format(a, l, ar, li))
print('\nAté a próxima !')
