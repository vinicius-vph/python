print('=' * 58)
print('Escreva algo e eu vou dizer as características desse dado')
print('=' * 58)
a = input('\nEscreva algo: ')
print('\nO dado informado {} está no formato:'.format(a), type(a))
print('É alfanumerico?', a.isalpha())
print('É numerico?', a.isnumeric())
print('É captalizado?',a.isidentifier())
print('É minuscula?', a.islower())
print('\nAté a próxima !')




