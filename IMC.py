# Programa para calcular o Índice de Massa Corporal (IMC)

# Solicita os dados do usuário
peso = float(input(f"Digite seu peso em kg: "))
altura = float(input(f"Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Determina a classificação e a recomendação
if imc < 18.5:
    classificacao = "Abaixo do peso"
    recomendacao = "Consulte um nutricionista para orientação"
elif imc < 25:
    classificacao = "Peso normal"
    recomendacao = "Mantenha hábitos saudáveis!"
elif imc < 30:
    classificacao = "Sobrepeso"
    recomendacao = "Considere uma dieta balanceada e atividade física"
elif imc < 35:
    classificacao = "Obesidade grau 1"
    recomendacao = "Procure orientação de um profissional de saúde"
elif imc < 40:
    classificacao = "Obesidade grau 2"
    recomendacao = "Consulte um médico para avaliação e orientação"
else:
    classificacao = "Obesidade grau 3"
    recomendacao = "Busque assistência médica imediatamente"

# Mostra o resultado
print(f"\nSeu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")
print(f"Recomendação: {recomendacao}")
