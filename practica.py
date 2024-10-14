numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))

suma = numero1 + numero2

print(f"La suma de {numero1} y {numero2} es: {suma}")


#ejemplo

resultado = float("55.1")
print(resultado)
print(type(resultado))


# Pedir al usuario el total de la cuenta y el porcentaje de propina
total_cuenta = float(input("Ingresa el total de la cuenta: $"))
porcentaje_propina = float(input("Ingresa el porcentaje de propina que deseas dejar: "))


# Calcular la propina
propina = (porcentaje_propina / 100) * total_cuenta


# Calcular el total a pagar
total_a_pagar = total_cuenta + propina


# Mostrar el resultado
print(f"\nPropina: ${propina:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")


##Ejemplo
cuenta = float(input("¿Cuánto se gastó en la comida?: "))
propina = float(input("¿Qué porcentaje de propina se quiere dejar?: "))
propina_a_pagar = propina * cuenta / 100
total_a_pagar = propina_a_pagar + cuenta
print("La cuenta fue de $", cuenta, ". La propina de ", propina, "% es de $", propina_a_pagar, ". El total a pagar es de $", total_a_pagar)
