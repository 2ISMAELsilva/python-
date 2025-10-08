# RETORNO DE SOMA DE 2 NUMEROS

numero1 = int(input('DIGITE UM NUMERO: '))
numero2 = int(input('DIGITE UM SEGUNDO NUMERO: '))

def soma(numero1, numero2):
    calcular = numero1 + numero2
    return calcular

def multiplicacao(numero1, numero2):
    calcular = numero1 * numero2
    return calcular

def divisao (numero1,numero2):
    calcular = numero1 / numero2
    return calcular

def subtracao(numero1,numero2):
    calcular = numero1 - numero2
    return calcular

def mostrar_resultado():
    print(f'O resultado da soma e: {somar}')
    print(f'O resultado da divição e: {div}')
    print(f'O resultado da multiplicação e: {mult}')
    print(f'O resultado da subtração e: {sub}')

somar = soma(numero1,numero2)
mult = multiplicacao(numero1,numero2)
div = divisao(numero1,numero2)
sub = subtracao(numero1,numero2)

mostrar_resultado()