# 

import os 
os.system ("cls")

print("""
Codigo \t prato \t\t\t valor
1 \t picanha \t\t R$ 25,00
2 \t lasanha \t\t R$ 20,00 
3 \t Strogonoff \t\t R$ 14,00 
4 \t Bife Acebolado \t R$ 15,00 
5 \t Pão com ovo \t\t R4 5,00
""")
codigo = int(input("DIgite o numero do pedido desejado. "))


prato = ""
valor = 0.0 

match codigo:
        case 1:
            prato = "picanha"
            valor = 25.00
        case 2:
            prato = "Lasanha"
            valor = 20.00 
        case 3: 
            prato = "Strogonoff"
            valor = 18.00 
        case 4:
            prato = "Bife Acebolado"
            valor = 15.00 
        case 5:
            prato = "Pão com Ovo"
            valor = 5.00
        case _:
          prato = "Prato invailido"

print("\n===Seu pedido===")
if valor is not None:
    print (f"prato escolhido: {prato}")
    print (f"Valor; R$ {valor:2.2f}")
else:
    print ("Prato invalido")