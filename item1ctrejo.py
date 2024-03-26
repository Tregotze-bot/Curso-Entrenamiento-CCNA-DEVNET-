def solicitar_datos():
    nombre = input("Por favor, introduce tu nombre: ")
    apellido = input("Por favor, introduce tu apellido: ")
    edad = input("Por favor, introduce tu edad: ")
    sede = input("Por favor, introduce tu sede: ")
    return nombre, apellido, edad, sede

def imprimir_datos(nombre, apellido, edad, sede):
    print("\nDatos ingresados:")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    print("Sede:", sede)

def main():
    print("Bienvenido. Por favor, introduce tus datos.")
    nombre, apellido, edad, sede = solicitar_datos()
    imprimir_datos(nombre, apellido, edad, sede)

if __name__ == "__main__":
    main()
