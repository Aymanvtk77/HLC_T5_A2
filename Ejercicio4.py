cr="secreta123"
intentos=0
lintentos=3
while intentos<lintentos:
    c=input("dime tu contraseña porfavor :)") 
    if cr == c:
        print("Hola")
        break
    else:
        intentos+=1
        print("contraseña incorrecta te quedan", lintentos-intentos , "intentos restantes")
        if intentos == lintentos:
            print("cuenta bloqueada XD") 