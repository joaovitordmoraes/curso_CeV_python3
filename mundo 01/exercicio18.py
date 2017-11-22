from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do ângulo: '))
print('O ângulo de {}º equivale a seno= {:.2f}, cosseno= {:.2f} e tangente= {:.2f}'.format(angulo, sin(radians(angulo)),
                                                                                           cos(radians(angulo)),
                                                                                           tan(radians(angulo))))


