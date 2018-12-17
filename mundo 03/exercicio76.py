'''
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
print('-'*41)
print(f'{"LISTAGEM DE PREÇOS": ^41}')
print('-'*41)
produtos = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for c in range(len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<31}R$', end='')
    else:
        print(f'{produtos[c]: >8.2f}')
print('-'*41)