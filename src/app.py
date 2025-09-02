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

            pwd = getpass.getpass(f"Escribe la contraseña correcta: ")

            if pwd==pwd_:
                print(f"CONTRASEÑA CORRECTA")
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
def datosCliente(NombreCli=(), Cc=()):
     NombreCli=input(f"Porfavor ingresa tu nombre: ")
     Cc = input(f"Porfavor ingresa tu C.C.: ")
     print()
     print()
     return NombreCli, Cc
NombreCli, Cc = datosCliente()
dclient=datosCliente()
print(dclient)

def serviciosSpa():
        #aquí creamos un diccionario donde tendremos una clave que será el número del 
        # Servicio, el cual el cliente podrá elegir, seguido del nombre y el valor del servicio.
    servicios={
            1:("Corte y cepillado:", 60000),
            2: ("Corte, cepillado y uñas:", 90000), 
            3:("Uñas en acrílico y cejas:", 100000), 
            4: ("Uñas en acrílico, maquillaje y cejas:", 140000)  

            }
       #en este punto mostramos por consola el listado de precios y servici
       # luego
    #print("\n".join(servicios))
    print(servicios)


    OpCli=int(input("¿Que servicio deseas? Selecciona el número del servicio: "))
    if OpCli in servicios:
        nombre_servicio, precio = servicios[OpCli]
        print(f"\n Servicio seleccionado: {nombre_servicio} - ${precio}")

        # Ahora pedimos el estrato
        estrato = int(input("Ingrese su estrato socioeconómico: "))

        # con este bloque calculamos el descuento dependiendo del estrato que el cliente proporcionó
        if estrato in [1, 2]:
            descuento = 0.15
        elif estrato in [3, 4]:
            descuento = 0.10
        else:
            descuento = 0.05

        valor_final = precio - (precio * descuento)
        return precio, descuento, valor_final
        

        #print(f"Nombre del cliente: {NombreCli}")
        #print(f"Cédula del cliente: {Cc}")
        #print(f" Precio original: ${precio}")
        #print(f" Descuento aplicado: {descuento*100}%")
        #print(f" Valor final a pagar: ${valor_final}")
#con esta parte del condicional, le arrojamos un mensaje al usuario, si ingresa un valor diferente a los servicios ofertados
    else:
        print("❌ Esa opción no existe en el menú")
precio, descuento, valor_final =serviciosSpa()
#prueba = datosCliente()
#serviciosSpa(prueba)
serspa=serviciosSpa()
print(serspa)

print(f"Nombre del cliente: {NombreCli}")
print(f"Cédula del cliente: {Cc}")
print(f" Precio original: ${precio}")
print(f" Descuento aplicado: {descuento*100}%")
print(f" Valor final a pagar: ${valor_final}")

print("ESTA ES LA CALCULADORA PARA LOS PRECIOS")
#print("PORFAVOR, PROPORCIONA TUS SIGUIENTES DATOS")

