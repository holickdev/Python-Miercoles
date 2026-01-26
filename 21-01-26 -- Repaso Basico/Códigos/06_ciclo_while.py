"""
===========================================
LECCIÓN 6: CICLO WHILE
===========================================
Aprende a repetir código mientras se cumpla una condición
"""

# ========================================
# CICLO WHILE BÁSICO
# ========================================

# Contar del 1 al 5
contador = 1
while contador <= 5:
    print("Contador:", contador)
    contador = contador + 1  # ¡IMPORTANTE! Incrementar el contador


# ========================================
# DIFERENCIA ENTRE FOR Y WHILE
# ========================================

# FOR: Cuando sabes cuántas veces repetir
print("\nCon FOR (sabemos que son 5 veces):")
for i in range(5):
    print(i)

# WHILE: Cuando no sabes cuántas veces repetir
print("\nCon WHILE (hasta que se cumpla una condición):")
numero = 1
while numero < 32:
    print(numero)
    numero = numero * 2  # Duplicar


# ========================================
# WHILE CON CONDICIONES
# ========================================

# Pedir un número hasta que sea positivo
print("\n--- Validar entrada ---")
numero = int(input("Ingresa un número positivo: "))

while numero <= 0:
    print("Error: El número debe ser positivo")
    numero = int(input("Intenta de nuevo: "))

print("¡Correcto! El número es:", numero)


# ========================================
# WHILE CON BREAK
# ========================================

# Salir del ciclo con break
print("\n--- Usando BREAK ---")
contador = 1
while True:  # Ciclo infinito
    print(contador)
    contador = contador + 1
    
    if contador > 5:
        break  # Salir del ciclo


# ========================================
# WHILE CON CONTINUE
# ========================================

# Saltar iteraciones con continue
print("\n--- Usando CONTINUE ---")
contador = 0
while contador < 10:
    contador = contador + 1
    
    if contador % 2 == 0:  # Si es par
        continue  # Saltar a la siguiente iteración
    
    print(contador)  # Solo imprime impares


# ========================================
# MENÚ INTERACTIVO
# ========================================

print("\n--- MENÚ INTERACTIVO ---")
opcion = ""

while opcion != "4":
    print("\n=== MENÚ ===")
    print("1. Saludar")
    print("2. Sumar dos números")
    print("3. Ver la hora")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print("¡Hola", nombre + "!")
    elif opcion == "2":
        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        print("Suma:", a + b)
    elif opcion == "3":
        print("Esta función aún no está disponible")
    elif opcion == "4":
        print("¡Hasta luego!")
    else:
        print("Opción no válida")


# ========================================
# EJERCICIO PRÁCTICO 1 - TAREA
# ========================================

"""
TAREA 6A: Juego de Adivinanza

DESCRIPCIÓN:
Crea un juego donde el usuario debe adivinar un número secreto.

El programa debe:
1. Tener un número secreto (por ejemplo, 7)
2. Pedir al usuario que adivine el número
3. Dar pistas: "Muy bajo" o "Muy alto"
4. Contar cuántos intentos tomó
5. Terminar cuando adivine correctamente

EJEMPLO DE EJECUCIÓN:
Adivina el número (1-10): 5
Muy bajo, intenta de nuevo
Adivina el número (1-10): 8
Muy alto, intenta de nuevo
Adivina el número (1-10): 7
¡Correcto! Lo adivinaste en 3 intentos

PISTAS:
- Usa while True para un ciclo infinito
- Usa break para salir cuando adivine
- Usa una variable para contar intentos
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 2 - TAREA
# ========================================

"""
TAREA 6B: Suma Progresiva hasta 100

DESCRIPCIÓN:
Crea un programa que sume números consecutivos hasta llegar a 100 o más.

El programa debe:
1. Empezar con suma = 0 y contador = 1
2. Ir sumando: 1, luego 2, luego 3, etc.
3. Mostrar cada suma parcial
4. Detenerse cuando la suma sea >= 100
5. Mostrar cuántos números se necesitaron

EJEMPLO DE EJECUCIÓN:
Sumando 1 - Total: 1
Sumando 2 - Total: 3
Sumando 3 - Total: 6
...
Sumando 14 - Total: 105
Se necesitaron 14 números para llegar a 100

REQUISITOS:
- Usa while suma < 100
- Incrementa el contador en cada iteración
"""

# Escribe tu código aquí:
