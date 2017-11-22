import random
from time import sleep
print('-=' * 10)
print('Vamos jogar Jokenpô?')
print('-=' * 10)

escolha = str(input('Escolha entre Pedra, Papel e Tesoura: ')).lower().strip()

print('JO')
sleep(1)
print('KEN')
sleep(2)
print('PO!!!')

lista = ['pedra', 'papel', 'tesoura']

escolhido = random.choice(lista)

if escolha == escolhido:
    print('Houve um empate, eu também escolhi {}'.format(escolhido))
elif escolha == 'tesoura' and escolhido == 'papel':
    print('Você venceu, eu escolhi {}'.format(escolhido))
elif escolha == 'tesoura' and escolhido == 'pedra':
    print('Eu venci, pois escolhi {}'.format(escolhido))
elif escolha == 'papel' and escolhido == 'pedra':
    print('Você venceu, eu escolhi {}'.format(escolhido))
elif escolha == 'papel' and escolhido == 'tesoura':
    print('Eu venci, pois escolhi {}'.format(escolhido))
elif escolha == 'pedra' and escolhido == 'tesoura':
    print('Você venceu, eu escolhi {}'.format(escolhido))
elif escolha == 'pedra' and escolhido == 'papel':
    print('Eu venci, pois escolhi {}'.format(escolhido))

