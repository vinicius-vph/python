#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
print('=' * 76)
print('Essa é uma calculadora de conversão de metros para centimetros e milimetros')
print('=' * 76)

a = float(input('\nDigite um valor em metros : '))
c = a * 100
m = a * 1000
print('\n{:.2f} metros tem {:.2f} centimetros e {:.2f} milimetros'.format(a, c, m))
print('\nAté a próxima !')