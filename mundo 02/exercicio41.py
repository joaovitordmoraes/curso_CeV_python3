from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - nascimento
abre = '\033[34m'
fecha = '\033[m'

if idade <= 9:
    print('Você é um atleta {}MIRIM{}'.format(abre, fecha))
elif idade <= 14:
    print('Você é um atleta {}INFANTIL{}'.format(abre, fecha))
elif idade <= 19:
    print('Você é um atleta {}JUNIOR{}'.format(abre, fecha))
elif idade == 20:
    print('Você é um atleta {}SÊNIOR{}'.format(abre, fecha))
else:
    print('Você é um atleta {}MASTER{}'.format(abre, fecha))

