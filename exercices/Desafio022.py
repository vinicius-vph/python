# crie um programa que leia o nome da pessoa e mostre
# o nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# quantas letras ao todo (sem considerar os espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome e o ultimo sobrenome: ')).strip()
print('\nEsse é o se nome todo maiusculo: ',nome.upper())
print('\nEsse é o seu nome minusculo: ',nome.lower())
print('\nSeu nome e sobrenome tem essa quantidade de letras: ',len(nome) - nome.count(' ') )
separado = nome.split()
print('\nSeu primeiro nome é: ',separado[0])
print('\nSeu primeiro nome tem essa quantidade de letras: ',len(separado[0]))
