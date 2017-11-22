salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    aumento = salario * 10/100
    novo = salario + aumento
else:
    aumento = salario * 15/100
    novo = salario + aumento
print('Seu salário com o aumento é de: R${:.2f}'.format(novo))