#escreva um programa que converta de Celsius para Farenheint
print('=' * 50)
print('Vamos converter graus Celsius em graus Fahrenheit')
print('=' * 50)
c = float(input('\nInforme uma temperatura em graus Celsius: '))
f = ((9 * c)/ 5) + 32
print('\nA temperatura de {} °C corresponde a {} °F'.format(c,f))
