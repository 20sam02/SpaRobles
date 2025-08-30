import sys 
import getpass

def validation():
        pwd_ = 123
        print(f"Bienvenido Admin")

        pwd = getpass.getpass("Escribe la contraseña correcta: ")

        if pwd_==pwd:
            print("BIENVENIDO AL SPA ROBLES")
        

        return
contra = validation()
print(contra)




print("ESTA ES LA CALCULADORA PARA LOS PRECIOS")
#print("PORFAVOR, PROPORCIONA TUS SIGUIENTES DATOS")

