#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome SANTO
print('=============================================')
print('Vamos analisar se sua cidade começa com SANTO')
print('=============================================\n')
cidade = str(input('Digite o nome da sua cidade: ')).lower().split()
print('santo'in cidade[0])
