n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Sua nota média foi de \033[31m{}\033[m.Você foi \033[31mREPROVADO\033[m.'.format(media))
elif (media >= 5.0) and (media <= 6.9):
    print('Sua nota média foi de \033[33m{}\033[m.Você esta em \033[33mRECUPERAÇÃO\033[m.'.format(media))
else:
    print('Sua nota média foi de \033[34m{}\033[m.Você foi \033[34mAPROVADO\033[m.'.format(media))
