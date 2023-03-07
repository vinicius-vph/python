#um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido
print('===================================================================================')
print('Você é um professor que quer sortear um dos seus quatro alunos para apagar o quadro')
print('===================================================================================\n')
from random import choice
aluno1 = input('Digite o nome do primeiro aluno(a): ')
aluno2 = input('Digite o nome do segundo aluno(a): ')
aluno3 = input('Digite o nome do terceiro aluno(a): ')
aluno4 = input('Digite o nome do quarto aluno(a): ')
sorteado = choice([aluno1,aluno2,aluno3,aluno4])
print('\nO aluno(a) sortudo selecionado para apagar o quadro foi \n##### {} !#####'.format(sorteado))
