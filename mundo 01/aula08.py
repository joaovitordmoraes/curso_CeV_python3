# import math
from math import sqrt
import emoji

print(emoji.emojize('Olá cocô :shit:', use_aliases=True))
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é {:.2f}'.format(num, raiz))
