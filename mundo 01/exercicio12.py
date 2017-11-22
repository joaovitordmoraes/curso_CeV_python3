preco = float(input('Qual o preço do produto? '))
desc = preco * (5/100)
subt = preco - desc
print('O valor com 5% de desconto é {:.2f}'.format(subt))
