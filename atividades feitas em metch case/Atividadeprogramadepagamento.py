import os 
os.system ("cls")


# Programa de pagamento com match case

# Solicita o valor do produto
valor_produto = float(input("Digite o valor do produto: R$ "))

# Solicita a forma de pagamento
print("\nEscolha a forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento à prazo")

opcao = int(input("Digite a opção (1 ou 2): "))


print("\n--- Resultado ---")

# Usando match-case
match opcao:
    case 1:
        # Pagamento à vista com desconto de 10%
        desconto = valor_produto * 0.10
        total = valor_produto - desconto
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print("Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    case 2:
        # Pagamento parcelado
        parcelas = int(input("Digite a quantidade de parcelas (até 6): "))
        if parcelas < 1 or parcelas > 6:
            print("Quantidade de parcelas inválida! Deve ser entre 1 e 6.")
        else:
            valor_parcela = valor_produto / parcelas
            print(f"Valor do produto: R$ {valor_produto:.2f}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_produto:.2f}")

    case _:
        print("Opção inválida!")
