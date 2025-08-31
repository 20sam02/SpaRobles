import sys 
import getpass

#en esta primera función realizaremos el validador de contraseña de usuario
def validation():
        pwd_ = "123"
        intentos = 0
        maxIntentos = 3
#el ciclo while nos ayudará a implementar un numero de oportunidades para ingresar al programa
        while intentos < maxIntentos:
            print(f"Bienvenido Admin")

            pwd = getpass.getpass("Escribe la contraseña correcta: ")

            if pwd==pwd_:
                print("CONTRASEÑA CORRECTA")
                return True
            else:
                print("CONTRASEÑA INCORRECTA")
                intentos += 1
#la siguiente función nos ayudará a cerrar el programa una vez se hayan errado las tres oportunidades para ingresar la contraseña
#he creado un else por fuera de el nivel del if para que el programa no se cierre con el primer incremento a la variable intentos
                #sys.exit()
        else: intentos == 1
        sys.exit()
            
        

        return
contra = validation()
print(contra)

#en esta segunda función pediremos al cliente que proporcione sus datos
def datosCliente():
     Nombre=input("Porfavor ingresa tu nombre: ")
     Cc = input("Porfavor ingresa tu C.C.: ")
     estrato=input("Porfavor ingresa tu estrato socioeconomico")
     servicioSpa=input("in")
     return
dclient=datosCliente()
print(dclient)


print("ESTA ES LA CALCULADORA PARA LOS PRECIOS")
#print("PORFAVOR, PROPORCIONA TUS SIGUIENTES DATOS")

