from datetime import date
ano = int(input('Digite o ano que você quer analisar. Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # VERIFICA SE O ANO ATUAL É BISSEXTO
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0: # VERIFICA SE O ANO É BISSEXTO
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
