'''
    EMPRESTIMO BANCÁRIO PARA A COMPRA DE UMA CASA
'''

valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = float(input('Em quantos anos pretende pagar? '))

prestacao = (valor / anos) / 12
parcelas = anos * 12

abre = '\033[31m'
fecha = '\033[m'

if prestacao <= (salario * 30/100):
    print('Empréstimo aprovado! Você deverá pagar {:.0f} parcelas de R${:.2f}'.format(parcelas, prestacao))
else:
    print('{}Empréstimo negado. O valor da parcela não pode exceder 30% do salário.{}'.format(abre, fecha))
