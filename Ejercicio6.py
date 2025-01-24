p = input("dime una palabra con alguno de los siguientes caracteres: @, #, $, % ")
ce = ['@', '#', '$', '%']
for caracter in ce:
    if caracter in p:
        print(f"La palabra tiene el símbolo {caracter}.")
        break
else:
    print("La palabra no tiene ninguno de los caracteres especiales.")