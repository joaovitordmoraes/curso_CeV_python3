cidade = str(input('Em que cidade você nasceu? ')).strip()
# palavra = cidade.title()
# print('Santo' in palavra)
palavra = cidade.title()
separar = palavra.split()
print('Santo' in separar[0])
