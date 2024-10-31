def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def comparar_con_promedio(numeros, promedio):
    for num in numeros:
        if num >= promedio: # faltaba :
            print(f"{num} es mayor que el promedio.")#faltaba un =
        elif num <= promedio: # faltaba :
            print(f"{num} es menor que el promedio.")#faltaba un =
        else: # faltaba :
            print(f"{num} es igual al promedio.")

# Pedir al usuario tres números
numeros = []
for i in range(3):
    num = int(input("Introduce un número: "))# esta guardando los datos del usuario como strings
    numeros.append(num)

# Calcular el promedio
promedio = calcular_promedio(numeros)

# Comparar cada número con el promedio
comparar_con_promedio(numeros, promedio)
