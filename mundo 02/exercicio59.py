'''
    Crie um programa que leia dois valores e mostre um menu na tela:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    Seu programa deverá realizar a operação solicitada em cada caso.
'''
opcao = 0
soma = 0
multiplicacao = 0
a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
while opcao != 5:
    print('''
Selecione uma das seguintes operações: 
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    ''')
    opcao = int(input('A opção selecionada: '))
    if opcao == 1:
        soma = a + b
        print('A soma dos números {} e {} é igual {}'.format(a, b, soma))
    if opcao == 2:
        multiplicacao = a * b
        print('A multiplicação dos números {} e {} é igual {}'.format(a, b, multiplicacao))
    if opcao == 3:
        maior = max(a, b)
        print('O maior dos dois números é: {}'.format(maior))
    if opcao == 4:
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
print('Fim.')