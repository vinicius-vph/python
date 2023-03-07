#desenvolva um programa que leia as notas de um aluno, e calcule e mostre sua média
print('=' * 55)
print('Digite suas notas e eu vou calcular sua média escolar!')
print('=' * 55)
print('')
a = float(input('\nDigite a sua primeira nota : '))
b = float(input('\nDigite a sua segunda nota : '))

if (a > 10) or (b > 10):
    print('\nValores invalidos digite uma nota entre 0 e 10')
    print('\nTente novamente !')

else:
    m = (a + b) / 2
    print('\nPrimeira Nota {}, Segunda Nota {}, logo a sua média é {:.1f}'.format(a, b, m))
    print('\nAté a próxima !')