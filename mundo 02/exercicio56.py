'''
    DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS.
    NO FINAL DO PROGRAMA, MOSTRE:
    1- A MÉDIA DA IDADE DO GRUPO
    2- QUAL É O NOME DO HOMEM MAIS VELHO
    3- QUANTAS MULHERES TÊM MENOS DE 20 ANOS
'''
media = 0
idademedia = 0
idademasc = 0
fem = 0
contf= 0
nomemasc= ''
for c in range(1, 5):
    print('{} PESSOA:'.format(c))

    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).upper().strip()

    #media de idades
    idademedia = (idade + idademedia)
    media = idademedia / c

    #verifica sexo
    if sexo == 'F':
        #conta quantidade de mulheres
        contf = contf + 1
        if idade < 20:
            fem = fem + 1

    if sexo == 'M':
        if idade > idademasc:
            idademasc = idade
            nomemasc = nome

    print('='*12)

print('A média das idades é de: {}'.format(media))
if contf == 0:
    print('Não foi registrada nenhuma mulher.')
else:
    if fem < 2:
        print('{} mulher tem menos de 20 anos.'.format(fem))
    else:
        print('{} mulheres tem menos de 20 anos.'.format(fem))
print('O nome do homem mais velho é: {}'.format(nomemasc))
