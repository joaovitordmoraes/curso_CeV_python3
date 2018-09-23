'''
    FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS.
    NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
'''
lista = []
for c in range(1, 6):
    pessoa = float(input('Digite o peso da {} pessoa: '.format(c)))
    lista.append(pessoa)
print('O maior peso foi {:.2f}Kg.'.format(max(lista)))
print('O menor peso foi {:.2f}Kg.'.format(min(lista)))
