from random import randint
from time import sleep
computador = randint(0, 5) # SORTEIA UM NÚMERO ENTRE 0 E 5
print('Escolhendo um número.......')
voce = int(input('Tente adivinhar em que número o computador pensou: '))
print('Processando...')
sleep(2)
if voce == computador:
    print('Você acertou!')
else:
    print('Você errou!')


