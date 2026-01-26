"""
===========================================
LECCIÓN 1: ENTRADA Y SALIDA DE DATOS
===========================================
Aprende a mostrar información y recibir datos del usuario
"""

# ========================================
# SALIDA: Mostrar información en pantalla
# ========================================

# La función print() muestra mensajes en la consola
print("¡Hola mundo!")
print("Este es mi primer programa en Python")

# Podemos mostrar varios valores separados por comas
print("Python", "es", "genial")

# Mostrar números
print("Mi número favorito es:", 42)


# ========================================
# ENTRADA: Recibir datos del usuario
# ========================================

# La función input() pide al usuario que escriba algo
nombre = input("¿Cuál es tu nombre? ")
print("¡Hola", nombre + "!")

# Pedir la edad
edad = input("¿Cuántos años tienes? ")
print("Tienes", edad, "años")


# ========================================
# CONVERTIR TEXTO A NÚMEROS
# ========================================

# input() siempre devuelve texto, debemos convertirlo a número
edad_texto = input("Ingresa tu edad: ")
edad_numero = int(edad_texto)  # Convertir texto a número entero

# Forma más corta (todo en una línea)
edad = int(input("¿Cuántos años tienes? "))

# Ahora podemos hacer operaciones matemáticas
print("El próximo año tendrás", edad + 1, "años")


# ========================================
# EJERCICIO PRÁCTICO - TAREA
# ========================================

"""
TAREA 1: Programa de Presentación Personal

DESCRIPCIÓN:
Crea un programa que pida al usuario la siguiente información:
1. Su nombre
2. Su color favorito
3. Su número favorito (debe ser un número entero)

Luego, el programa debe mostrar:
- Un saludo personalizado con el nombre
- El color favorito
- El número favorito multiplicado por 2

EJEMPLO DE EJECUCIÓN:
¿Cómo te llamas? Juan
¿Cuál es tu color favorito? azul
¿Cuál es tu número favorito? 7

Hola Juan
Tu color favorito es azul
Tu número favorito multiplicado por 2 es: 14

PISTA:
- Usa input() para pedir datos
- Usa int() para convertir el número
- Usa print() para mostrar los resultados
"""

# Escribe tu código aquí:
