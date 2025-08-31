import sys 
import getpass

def validation():
        pwd_ = "123"
        intentos = 0
        maxIntentos = 3
        
        while intentos < maxIntentos:
            print(f"Bienvenido Admin")

            pwd = getpass.getpass("Escribe la contraseña correcta: ")

            if pwd==pwd_:
                print("CONTRASEÑA CORRECTA")
                return True
            else:
                print("CCONTRASEÑA INCORRECTA")
                intentos += 1
            

        return
contra = validation()
print(contra)




print("ESTA ES LA CALCULADORA PARA LOS PRECIOS")
#print("PORFAVOR, PROPORCIONA TUS SIGUIENTES DATOS")

