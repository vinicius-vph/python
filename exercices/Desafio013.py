#faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
print('=' * 130)
print('Esse ano foi aprovado 15 % de discidio pelo seu sindicato, informe o valor do seu salário e nós calcularemos o seu novo salário !')
print('=' * 130)

a = float(input('Digite o valor do seu salário e nós calcularemos o seu discidio esse ano : R$ '))
b = a * 0.15
c = a + b
print('\nO seu salário foi aumentado para R$ {:.2f}.'.format(c))
print('\nAté a próxima !')

