import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 50)
    adivinado = False

    print("Adivina el número que esta entre 1 y 50:")

    while not adivinado:
        intento = input("Introduce la adivinanza: ")
        
        intento = int(intento)

        if intento < numero_secreto:
            print("mas alto")
        elif intento > numero_secreto:
            print("mas bajo")
        else:
            print("Correcto")
            adivinado = Verdad

if __name__ == "__main__":
    adivina_el_numero()