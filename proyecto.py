import getpass  # Importar el módulo getpass para ocultar la entrada de la contraseña


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
            print("Estás por debajo del peso apropiado.")
            print("Te recomiendo un nutricionista y un entrenamiento de dos veces por semana.")
            print("Por favor, pregúntale a Lu cuál es su objetivo.")
            print("Número de contacto del nutricionista Lu: 112244556677")
        
        elif imc <= 24.9:
            print("Eres saludable.")
            print("Te recomiendo un entrenamiento de 4 veces por semana.")
            print("Por favor, pregúntale cuál es su objetivo.")
        
        elif imc <= 29.9:
            print("Tienes sobrepeso.")
            print("Te recomiendo entrenar 3 veces por semana.")
            print("Por favor, pregúntale cuál es su objetivo.")
        
        elif imc <= 34.9:
            print("Tienes obesidad tipo 1.")
            print("Te recomiendo entrenar 3 veces por semana.")
            print("Por favor, pregúntale cuál es su objetivo.")
        
        elif imc <= 39.9:
            print("Tienes obesidad tipo 2.")
            print("Te recomiendo entrenar 3 veces por semana.")
            print("Por favor, pregúntale cuál es su objetivo.")
        
        elif imc >= 40:
            print("Tienes obesidad tipo 3.")
            print("Te recomiendo entrenar 3 veces por semana.")
            print("Por favor, pregúntale cuál es su objetivo.")


        # Mostrar el costo por clase
        costo_por_clase = 19100
        print(f"El monto por clase es: {costo_por_clase}.")


        # Preguntar cuántos días quieren entrenar por semana
        dias_entrenamiento = int(input("¿Cuántos días quieres entrenar por semana? (1-7): "))
        if 1 <= dias_entrenamiento <= 7:
            total_costo = dias_entrenamiento * costo_por_clase
            print(f"Si entrenas {dias_entrenamiento} día(s) a la semana, el costo total será: {total_costo}.")
        else:
            print("Número de días no válido. Por favor ingresa un número entre 1 y 7.")
    elif imc_response == "no":
        print("Está bien, si cambias de opinión, estamos aquí para ayudarte.")
    else:
        print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")
else:
    print("Sos menor de edad, busca a una persona mayor para continuar.")
    exit()  # Salir del programa si el usuario es menor de edad
