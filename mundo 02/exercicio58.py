'''
    Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
    palpites foram necessários para vencer.
'''
from random import randint
from time import sleep

palpites = 0
palpite = 0
computador = randint(0, 10)
print('Escolhendo um número....')
while palpite != computador:
    palpite = int(input('Tente adivinhar em que número o computador pensou: '))
    palpites = palpites + 1
    sleep(2)
    print('Processando...')
    if palpite == computador:
        print('Você acertou!')
        if palpites < 2:
            print('Você precisou de {} tentativa para acertar, Parabéns!'.format(palpites))
        else:
            print('Você precisou de {} tentativas para acertar, você precisa melhorar!'.format(palpites))
    else:
        print('Você errou, tente novamente!')



