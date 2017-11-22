nome = str(input('Digite seu nome completo: ')).strip()
arrumar = nome.title()
dividir = arrumar.split()
print('Você possui Silva em seu nome? {}'.format('Silva' in dividir))
