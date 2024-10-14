user_name = input("Ingresa tu nombre ")
user_lastname = input("Ingresa tu apellido ")


print("Bienvenido", user_name, user_lastname)


user_age = int(input("Ingresa tu edad "))  


if user_age >= 18:
    print("Sos mayor de edad")
    
    imc_response = input("¿Querés saber tu IMC? Para poder ayudarte mejor en tu selección de entrenamiento (sí/no): ").lower()
    
    if imc_response == "sí" or imc_response == "si":  
        user_weight = float(input("Ingresa tu peso en kg: "))  
        user_height = float(input("¿Cuál es tu altura en metros? (por ejemplo, 1.75): "))  
        
        
        imc = user_weight / (user_height ** 2)
        print(f"Tu IMC es {imc:.2f}.")
        
     
        if imc < 18.5:
            print("Estás por debajo del peso apropiado.")
        elif imc <= 24.9:
            print("Eres saludable.")
        elif imc <= 29.9:
            print("Tienes sobrepeso.")
        elif imc <= 34.9:
            print("Tienes obesidad tipo 1.")
        elif imc <= 39.9:
            print("Tienes obesidad tipo 2.")
        elif imc >= 40:
            print("Tienes obesidad tipo 3.")
        else:
            print("Puede que no ingresaste un dato o ingresaste un dato inválido.")
        
    elif imc_response == "no":
        print("Está bien, si cambias de opinión, estamos aquí para ayudarte.")
    else:
        print("Respuesta no válida. Por favor, responde 'sí' o 'no'.")
else:
    print("Sos menor de edad, busca a una persona mayor para continuar")
    exit()  
