'''
    Crie um programa que leia vários números inteiros pelo teclado.
    No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
    O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''
n = cont = soma = media = maior = menor = 0
opcao = 'Ss'
while opcao in 'Ss':
    n = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar [S/N]? ')).strip()
    soma += n
    if n > maior:
        maior = n
    if n < maior:
        menor = n
        if n < menor:
            menor = n
    cont += 1
media = soma / cont
print('Você digitou {} números e a média entre eles foi de {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Fim.')