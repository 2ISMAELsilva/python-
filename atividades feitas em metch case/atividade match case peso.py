

genero = input("QUAL SEU GENERO? (Masculino(M) OU Femenino(F)): ")
Altura = float(input("Qual A SUA ALTURA? "))

match genero:
    case 'm':
        resultado = (72.7 * Altura) - 58
        print(f"SEU PESO IDEAL E: {resultado: .2f}") 
    case 'f': 
        resultado = (62.1 * Altura) - 44.7
        print(f"SEU PESO IDEAL E: {resultado: .2f}")  