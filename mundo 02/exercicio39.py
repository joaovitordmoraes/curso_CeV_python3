from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year

if (atual - ano) < 18:
    calculo = atual - ano
    tempo = 18 - calculo
    print('Ainda faltam {} anos para você se alistar para o serviço militar.'.format(tempo))
elif (atual - ano) == 18:
    print('É hora de você se alistar para o serviço militar.')
else:
    calculo = atual - ano
    tempo = calculo - 18
    print('Fazem {} anos que você já passou do tempo do alistamento militar.'.format(tempo))

