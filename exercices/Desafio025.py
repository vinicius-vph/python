#Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome
print('=========================================')
print('Vamos verificar se você tem SILVA no nome')
print('=========================================\n')
nome = str(input('Digite seu nome: '))
print('silva' in nome.lower())