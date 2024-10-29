# Mensaje de bienvenida 
print("Bienvenido, a YesFitness")


# Lista de productos iniciales
lista_producto = [
    {"nombre": "Full Body", "precio": 19100, "stock": 10},
    {"nombre": "Upper Body", "precio": 19100, "stock": 10},
    {"nombre": "Lower Body", "precio": 19100, "stock": 10},
    {"nombre": "Abs", "precio": 19100, "stock": 10},
    {"nombre": "Yoga", "precio": 19100, "stock": 10},
    {"nombre": "Stretching", "precio": 19100, "stock": 10},
    {"nombre": "Aerobics", "precio": 19100, "stock": 10},
]


# Interacción con el usuario
user_name = input("Ingresa tu nombre: ")
user_lastname = input("Ingresa tu apellido: ")


print("Bienvenido", user_name, user_lastname)


user_age = int(input("Ingresa tu edad: "))  # Convertir la entrada a un entero


if user_age >= 18:
    print("Sos mayor de edad")


    # Preguntar si el usuario quiere saber su IMC
    imc_response = input("¿Querés saber tu IMC? Para poder ayudarte mejor en tu selección de entrenamiento (sí/no): ").lower()


    if imc_response == "sí" or imc_response == "si":  # Aceptar tanto "sí" como "si"
        user_weight = float(input("Ingresa tu peso en kg: "))  # Pedir el peso en kg
        user_height = float(input("¿Cuál es tu altura en metros? (por ejemplo, 1.75): "))  # Pedir la altura en metros
        
        # Calcular IMC
        imc = user_weight / (user_height ** 2)
        print(f"Tu IMC es {imc:.2f}.")
        
        # Clasificación del IMC
        if imc < 18.5:
            print("Estás por debajo del peso apropiado. Te recomiendo un nutricionista y un entrenamiento de dos veces por semana.")
        elif imc <= 24.9:
            print("Eres saludable. Te recomiendo un entrenamiento de 4 veces por semana.")
        elif imc <= 29.9:
            print("Tienes sobrepeso. Te recomiendo entrenar 3 veces por semana.")
        elif imc <= 34.9:
            print("Tienes obesidad tipo 1. Te recomiendo entrenar 3 veces por semana.")
        elif imc <= 39.9:
            print("Tienes obesidad tipo 2. Te recomiendo entrenar 3 veces por semana.")
        elif imc >= 40:
            print("Tienes obesidad tipo 3. Te recomiendo entrenar 3 veces por semana.")


        # Menú de opciones
        opcion = 0
        
        while opcion != 4:
            print("\nMenú de Opciones")
            print("\t1. Mostrar el valor por clase")
            print("\t2. Elegir días de entrenamiento")
            print("\t3. Ver días elegidos y el total")
            print("\t4. Salir")
            
            opcion = int(input("Seleccioná una opción: "))
            
            if opcion == 1:
                print(f"El monto por clase es: {lista_producto[0]['precio']}.")


            elif opcion == 2:
                dias_disponibles = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
                dias_elegidos = []  # Lista para guardar los días y productos elegidos


                dias_entrenamiento = int(input("¿Cuántos días quieres entrenar por semana? (1-7): "))
                
                if 1 <= dias_entrenamiento <= 7:
                    # Elegir los días de entrenamiento
                    for i in range(dias_entrenamiento):
                        dia = input(f"Seleccioná el día {i + 1} (lunes a domingo): ").lower()
                        if dia in dias_disponibles:
                            print("Tipos de entrenamiento disponibles:")
                            for j, producto in enumerate(lista_producto):
                                print(f"{j + 1}. {producto['nombre']} - Precio: {producto['precio']}")


                            tipo_entrenamiento = int(input("Selecciona el número del tipo de entrenamiento que deseas para este día: ")) - 1
                            if 0 <= tipo_entrenamiento < len(lista_producto):
                                dias_elegidos.append((dia, lista_producto[tipo_entrenamiento]["nombre"]))
                            else:
                                print("Número de tipo de entrenamiento no válido. Intenta de nuevo.")
                        else:
                            print(f"'{dia}' no es un día válido. Intenta de nuevo.")
                else:
                    print("Número de días no válido. Por favor ingresa un número entre 1 y 7.")
                
            elif opcion == 3:
                # Ver días seleccionados y el total
                if dias_elegidos:
                    total_costo = len(dias_elegidos) * lista_producto[0]["precio"]
                    print(f"El costo total por los días seleccionados:")
                    for dia, tipo in dias_elegidos:
                        print(f"{dia}: {tipo}")
                    print(f"Total: {total_costo}.")
                else:
                    print("No has seleccionado ningún día de entrenamiento.")
                
            elif opcion == 4:
                print("Saliendo del menú.")
            else:
                print("Opción no válida. Por favor, ingresá una opción entre 1 y 4.")
    
    elif imc_response == "no":
        print("Está bien, si cambias de opinión, estamos aquí para ayudarte.")
    else:
        print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")
else:
    print("Sos menor de edad, busca a una persona mayor para continuar.")
    exit()  # Salir del programa si el usuario es menor de edad


# Mostrar la lista de productos al final (opcional)
print("\nProductos disponibles:")
for producto in lista_producto:
    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
