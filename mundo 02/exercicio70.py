'''
    Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar ou não.
    No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato.
'''
produto = continuar = barato = ''
preco = soma = maior = menor = cont = 0
print('-'*40)
print('{:-^40}'.format(' LOJA SUPER BARATÃO '))
print('-'*40)
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$ '))
    cont += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    soma += preco
    if preco > 1000:
        maior += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if continuar == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi de R${soma:.2f}')
print(f'Temos {maior} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')