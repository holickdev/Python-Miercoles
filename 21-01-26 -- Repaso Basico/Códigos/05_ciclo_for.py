"""
===========================================
LECCIÓN 5: CICLO FOR
===========================================
Aprende a repetir código un número determinado de veces
"""

# ========================================
# CICLO FOR BÁSICO
# ========================================

# Repetir 5 veces (de 0 a 4)
print("Contando del 0 al 4:")
for i in range(5):
    print(i)


# ========================================
# CICLO FOR CON INICIO Y FIN
# ========================================

# Contar del 1 al 5
print("\nContando del 1 al 5:")
for i in range(1, 6):
    print(i)

# Contar del 10 al 15
print("\nContando del 10 al 15:")
for i in range(10, 16):
    print(i)


# ========================================
# CICLO FOR CON SALTOS
# ========================================

# Contar de 2 en 2
print("\nNúmeros pares del 0 al 10:")
for i in range(0, 11, 2):
    print(i)

# Contar de 5 en 5
print("\nContando de 5 en 5:")
for i in range(0, 26, 5):
    print(i)

# Contar hacia atrás
print("\nCuenta regresiva:")
for i in range(10, 0, -1):
    print(i)
print("¡Despegue!")


# ========================================
# USAR EL CONTADOR EN OPERACIONES
# ========================================

print("\nTabla del 5:")
for i in range(1, 11):
    resultado = 5 * i
    print("5 x", i, "=", resultado)


# ========================================
# ACUMULAR VALORES
# ========================================

# Sumar números del 1 al 10
suma = 0
for i in range(1, 11):
    suma = suma + i
    print("Suma parcial:", suma)

print("Suma total:", suma)


# ========================================
# CICLOS ANIDADOS
# ========================================

print("\nPatrón de asteriscos:")
for fila in range(1, 6):
    for columna in range(fila):
        print("*", end="")  # end="" evita el salto de línea
    print()  # Salto de línea al final de cada fila


# ========================================
# EJERCICIO PRÁCTICO 1 - TAREA
# ========================================

"""
TAREA 5A: Generador de Tablas de Multiplicar

DESCRIPCIÓN:
Crea un programa que muestre la tabla de multiplicar de un número.

El programa debe:
1. Pedir al usuario qué tabla quiere ver
2. Mostrar la tabla del 1 al 10
3. Usar un ciclo for

EJEMPLO DE EJECUCIÓN:
¿Qué tabla quieres ver? 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50

PISTA:
- Usa range(1, 11) para ir del 1 al 10
- Multiplica el número por i en cada iteración
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 2 - TAREA
# ========================================

"""
TAREA 5B: Sumador de Números

DESCRIPCIÓN:
Crea un programa que sume varios números ingresados por el usuario.

El programa debe:
1. Preguntar cuántos números se van a sumar
2. Pedir cada número usando un ciclo for
3. Ir acumulando la suma
4. Mostrar el resultado final

EJEMPLO DE EJECUCIÓN:
¿Cuántos números quieres sumar? 3
Número 1: 10
Número 2: 20
Número 3: 15
La suma total es: 45

REQUISITOS:
- Usa una variable para acumular la suma (inicializada en 0)
- Usa range() con la cantidad ingresada
"""

# Escribe tu código aquí:
