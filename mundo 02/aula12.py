nome = str(input('Qual é seu nome? '))
if nome == 'João':
    print('Que nome bonito!')
elif nome == 'Gabriela':
    print('Nossa, como você é gata, gata!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
