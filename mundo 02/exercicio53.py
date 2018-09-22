'''
    CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM PALÍNDROMO,
    DESCONSIDERANDO OS ESPAÇOS.
'''
from time import sleep
frase = str(input('Digite uma frase: ')).lower().strip()
separar = frase.split()
juntar = ''.join(separar)
print('Comparando...')
sleep(3)
print('Frases comparadas: {} e {}'.format(juntar, juntar[::-1]))
sleep(3)
if juntar == juntar[::-1]:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo.')