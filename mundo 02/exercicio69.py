'''
    Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
    o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    A) quantas pessoas tem mais de 18 anos.
    B) quantos homens foram cadastrados.
    C) quantas mulheres tem menos de 20 anos.
'''

i = maioridade = h = m = 0
s = continuar = ''
while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    i = int(input('Idade: '))
    s = str(input('Sexo: [M/F] ')).strip().upper()
    print('-'*25)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if i >= 18:
        maioridade += 1
    if s == 'M':
        h += 1
    if i < 20 and s == 'F':
        m += 1
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maioridade}')
print(f'Ao todo temos {h} homens cadastrados')
print(f'E temos {m} mulheres com menos de 20 anos')