#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento 
#para salarios superiores a R$ 1250,00 calcule um aumento de 10%
#para inferiores ou iguais o aumento é de 15%
print('================================================================')
print('            Vamos calcular seu aumento salarial...')
print('         O discidio foi concedido da seguinte maneira')
print('\n**************************************************************')
print('* Salários inferiores ou iguais à R$ 1250 o aumento é de 15% *')
print('* Salários superiores à R$ 1250 o aumento é de 10%           *')
print('**************************************************************')
print('\n===============================================================\n')
salario = float(input('Vamos calcular o valor do seu salário com o aumento.\n\nDigite o seu salário R$ '))
if salario > 1250:
    print('\nSeu novo salário é R$ {:.2f}'.format(salario *1.1))
else:
	print('\nSeu novo salário é R$ {:.2f}'.format(salario * 1.15))