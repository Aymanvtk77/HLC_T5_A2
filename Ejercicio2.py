
numero_1 = float(input("Introduce el primer número porfavor:"))
numero_2 = float(input("Introduce el segundo número porfavor:"))
numero_3 = float(input("Introduce el tercer número porfavor:"))

if numero_1 == numero_2 == numero_3:
    print(f"todos los numeros son iguales: {numero_1}")
elif numero_1 == numero_2 and numero_1 > numero_3:
    print(f"hay un empate entre los mayores: {numero_1} y {numero_2}")
elif numero_1 == numero_3 and numero_1 > numero_2:
    print(f"hay un empate entre los mayores: {numero_1} y {numero_3}")
elif numero_2 == numero_3 and numero_2 > numero_1:
    print(f"hay un empate entre los mayores: {numero_2} y {numero_3}")
else:
    mayor = max(numero_1, numero_2, numero_3)
    print(f"el mayor numero es: {mayor}")