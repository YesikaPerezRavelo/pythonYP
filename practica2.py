# Función para calcular litros consumidos y costo total del viaje
def calcular_combustible(consumo_por_100_km, costo_por_litro, longitud_viaje_km):
    # Calcular los litros consumidos
    litros_consumidos = (consumo_por_100_km / 100) * longitud_viaje_km
    # Calcular el costo total del combustible
    costo_total_combustible = litros_consumidos * costo_por_litro
    return litros_consumidos, costo_total_combustible


# Datos de entrada
consumo_por_100_km = 12  # Litros por cada 100 km
costo_por_litro = 1021  # Precio en la moneda local por litro
longitud_viaje_km = 350  # Distancia del viaje en kilómetros


# Llamada a la función
litros_consumidos, costo_total_combustible = calcular_combustible(consumo_por_100_km, costo_por_litro, longitud_viaje_km)


# Mostrar resultados
print(f"Litros consumidos: {litros_consumidos:.2f} L")
print(f"Dinero gastado: {costo_total_combustible:.2f}")
