preco = float(input('Qual o preço do produto? R$'))
forma = str(input('Qual a forma de pagamento (à vista ou parcelado)? ')).strip()

red = '\033[31m'
fecha = '\033[m'

if forma == 'à vista' or forma == 'a vista':
    print('À vista selecionado.')
    avista = str(input('Será pago em dinheiro, cheque ou cartão? ')).strip()
    if avista == 'dinheiro' or avista == 'cheque':
        desconto = preco - (preco * (10/100))
        print('O valor total a ser pago é de R${:.2f}'.format(desconto))
    elif avista == 'cartão' or avista == 'cartao':
        desconto = preco - (preco * (5/100))
        print('O valor total a ser pago é de R${:.2f}'.format(desconto))
    else:
        print('{}Forma de pagamento inválida.{}'.format(red, fecha))
elif forma == 'parcelado':
    print('Parcelado selecionado.')
    parcelas = int(input('Em quantas parcelas deseja dividir no cartão? '))
    if parcelas == 2:
        print('O valor total a ser pago é de R${:.2f}'.format(preco))
    elif parcelas >= 3:
        juros = preco + (preco * (20/100))
        print('O valor total a ser pago é de R${:.2f}'.format(juros))
    else:
        print('{}Forma de pagamento inválida.{}'.format(red, fecha))
else:
    print('{}Forma de pagamento inválida.{}'.format(red, fecha))

