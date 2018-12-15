'''
    Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
    Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        print('Número inválido, por favor digite um número entre 0 e 20.')
    else:
        print(f'O número que você digitou foi o {numeros[n]}.')
        decisao = str(input('Você deseja continuar? [S/N] '))
        if decisao in 'Nn':
            break
print('PROGRAMA ENCERRADO.')