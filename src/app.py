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
                print()
                print()
                return True
                
            else:
                print("CONTRASEÑA INCORRECTA")
                intentos += 1
            print()
            print()
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
     estrato=input("Porfavor ingresa tu estrato socioeconomico: ")
     print()
     print()
     return
dclient=datosCliente()
print(dclient)

def serviciosSpa():
       
       tabladeprecios={opcion1}
       
       opcion1=int(60000) 
       opcion2=int(90000) 
       opcion3=int(100000) 
       opcion4=int(140000)  
       servicios=[
            "1. Corte y cepillado: $60.000",
            "2. Corte, cepillado y uñas: $90.000", 
            "3. Uñas en acrílico y cejas: $100.000", 
            "4. Uñas en acrílico, maquillaje y cejas: $ 140.000"  

       ]
       print("\n".join(servicios))
       OpCli=input("¿Que servicio deseas? Selecciona el número del servicio: ")
       


       #print(opcion1,opcion2,opcion3,opcion4)

serspa=serviciosSpa()
print(serspa)


print("ESTA ES LA CALCULADORA PARA LOS PRECIOS")
#print("PORFAVOR, PROPORCIONA TUS SIGUIENTES DATOS")

