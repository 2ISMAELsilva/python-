import os 
os.system('cls')


total = 0
escolha = "s"

while escolha.lower() == "s":
    # Mostrar o menu com print
    print("\nCardápio:")
    print("1 - Picanha         - R$ 25,00")
    print("2 - Lasanha         - R$ 20,00")
    print("3 - Strogonoff      - R$ 18,00")
    print("4 - Bife Acebolado  - R$ 15,00")
    print("5 - Pão com ovo     - R$  5,00")

    try:
        codigo = int(input("\nDigite o código do prato desejado: "))
        
        if codigo == 1:
            print("Você escolheu: Picanha - R$ 25,00")
            total += 25.00
        elif codigo == 2:
            print("Você escolheu: Lasanha - R$ 20,00")
            total += 20.00
        elif codigo == 3:
            print("Você escolheu: Strogonoff - R$ 18,00")
            total += 18.00
        elif codigo == 4:
            print("Você escolheu: Bife Acebolado - R$ 15,00")
            total += 15.00
        elif codigo == 5:
            print("Você escolheu: Pão com ovo - R$ 5,00")
            total += 5.00
        else:
            print("Código inválido!")

    except ValueError:
        print("Entrada inválida. Digite um número.")

    escolha = input("Deseja escolher outro prato? (s/n): ")

print(f"\nTotal a pagar: R$ {total:.2f}")

os.system('cls')