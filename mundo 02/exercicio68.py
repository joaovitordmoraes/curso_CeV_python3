'''
    Faça um programa que jogue par ou ímpar com o computador.
    O jogo só será interrompido quando o jogador perder, mostrando
    o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
print('=-'*16)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-'*16)
v = cont = s = 0
c = randint(0, 10)
escolha = comp = ''
resultado = ''
while True:
    v = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    s = v + c
    if s % 2 == 0:
        comp = 'P'
        resultado = 'PAR'
    else:
        comp = 'I'
        resultado = 'ÍMPAR'
    print('-'*32)
    print(f'Você jogou {v} e o computador {c}. Total de {s} -> RESULTADO {resultado}')
    print('-'*32)
    if escolha == comp:
        print('Você VENCEU!')
        print('Vamos jogar novamente....')
        print('=-' * 16)
        cont += 1
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        print('=-' * 16)
        break

