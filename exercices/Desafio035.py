#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo, formula de triangulos
print('∆' *41)
print('\nVamos calcular se 3 retas conseguem\nou não formar um triângulo com as medidas\nem centímetros dadas!\n')
print('∆' *41)

r1 = float(input('\nDigite a reta 1: '))
r2 = float(input('\nDigite a reta 2: '))
r3 = float(input('\nDigite a reta 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\nOs seguimentos podem formar um triângulo')
else:
    print('\nOs seguimentos não pode formar um triângulo')
