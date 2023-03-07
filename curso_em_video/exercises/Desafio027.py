#Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o ultimo nome separadamente
#Ex.: Ana maria de Souza, primeiro: Ana, ultimo: Souza
print('==========================================')
print('Vamos separar o seu primeiro e último nome')
print('==========================================\n')
nome = str(input('Digite seu nome completo: '))
nome = nome.split()
print('\nOlá',nome[0],nome[-1])

