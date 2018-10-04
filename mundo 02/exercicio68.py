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
escolha = ''
resultado = ''
while True:
    v = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    s = v + c
    if s % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'Você jogou {v} e o computador {c}. Total de {s} -> RESULTADO {resultado}')
    if escolha == resultado:
        print('Você VENCEU!')
        print('Vamos jogar novamente....')
        cont += 1
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break

