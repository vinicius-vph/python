#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado, calcule o preço,
#sabendo que  o carro custa R$ 60 por dia e 0,15 por km rodado
space = ' ' * 12
print('=' * 65)
print('Vamos calcular o custo que você terá ao alugar um carro conosco')
print('sabendo que  o carro custa \n')
print(space + '*' * 25)
print(space + '* R$ 60 por dia         *')
print(space + '* R$ 0,15 por km rodado *')
print(space + '*' * 25)
print('=' * 65)
dias = int(input('\nInforme o número de dias de aluguel: '))
km = float(input('Informe o numero de km rodados: '))
custo = ((60*dias)+(0.15*km))
print('\nSeu aluguel foi de {} dias, sendo {} km rodados, seu custo total do aluguel foi de R$ {:.2f}'.format(dias, km, custo))