import string
import random

# Obtener la longitud de la contraseña
longitud = int(input("Ingrese la longitud de la contraseña: "))

print('''Elija el conjunto de caracteres para la contraseña de estas opciones:
        1. Dígitos
        2. Letras
        3. Caracteres especiales
        4. Salir''')

listaCaracteres = ""

# Obtener el conjunto de caracteres para la contraseña
while True:
    opcion = int(input("Elija un número: "))
    if opcion == 1:
        # Agregar letras a los caracteres posibles
        listaCaracteres += string.ascii_letters
    elif opcion == 2:
        # Agregar dígitos a los caracteres posibles
        listaCaracteres += string.digits
    elif opcion == 3:
        # Agregar caracteres especiales a los caracteres posibles
        listaCaracteres += string.punctuation
    elif opcion == 4:
        break
    else:
        print("¡Por favor elija una opción válida!")

contraseña = []

for i in range(longitud):
    # Elegir un carácter aleatorio de nuestra lista de caracteres
    caracterAleatorio = random.choice(listaCaracteres)
    
    # Agregar un carácter aleatorio a la contraseña
    contraseña.append(caracterAleatorio)

# Imprimir la contraseña como una cadena
print("La contraseña aleatoria es: " + "".join(contraseña))
