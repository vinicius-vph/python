#o mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
#faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import sample,shuffle
print('===============================================================================')
print('Vamos sortear a sequência na qual os alunos vão apresentar o trabalho escolares')
print('===============================================================================\n')
print('Digite abaixo o nome dos alunos para o sorteio.')
#modo 1
aluno1 = input('\nNome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
apresentacao = sample([aluno1,aluno2,aluno3,aluno4], k=4)
print('\nA sequência de apresentação dos trabalhos é a seguinte:\n{}'.format(apresentacao))
#modo2
aluno1 = input('\nNome do aluno:')
aluno2 = input('Nome do aluno:')
aluno3 = input('Nome do aluno:')
aluno4 = input('Nome do aluno:')
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('\nA ordem de apresentação sera:')
print(lista)