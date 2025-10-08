# Algoritimo que solicita um valor em metros e corresponde em centimetros 

import os 
os.system('cls')

def metros_p_centimentros(metros):
    return metros * 100

metros = float(input('DIGITE OS VALORES EM METROS'))
valor_centimetro = metros_p_centimentros(metros)
print (f'{metros}Metros são equivalemtes a {valor_centimetro}')

