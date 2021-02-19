#faça um programa que leia uma frase pelo teclado e mostre :
#Quantas vezes a eletra "A" aparece
#Em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez
print('============================================================')
print('Digite uma frase e diremos quantas vezes a letra A aparece')
print('============================================================\n')
frase = str(input('Digite uma frase qualquer: ')).strip()
print('\nSua frase tem',frase.lower().count('a'),'letras A',)
print('A letra a aparece pela primeira vez na posição',frase.find('a'),'e pela útima vez na posição',frase.rfind('a'))

