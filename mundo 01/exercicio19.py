import random
aluno1 = input('Digite o nome do primero aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('O professor selecionou o aluno {}, para apagar o quadro.'.format(random.choice(lista)))
