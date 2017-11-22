nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
dividido = nome.split()
# print(len(''.join(dividido)))
# print('Seu nome tem o total de {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu nome tem o total de {} letras.'.format(len(''.join(dividido))))
print('Seu primeiro nome tem {} letras.'.format(len(dividido[0])))




