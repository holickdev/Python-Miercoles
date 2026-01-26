"""
===========================================
LECCIÓN 4: ESTRUCTURAS CONDICIONALES
===========================================
Aprende a tomar decisiones en tu código
"""

# ========================================
# CONDICIONAL SIMPLE (IF)
# ========================================

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

print("Este mensaje siempre se muestra")


# ========================================
# CONDICIONAL CON ELSE
# ========================================

edad = 15

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# ========================================
# CONDICIONAL CON ELIF
# ========================================

calificacion = 85

if calificacion >= 90:
    print("Excelente - A")
elif calificacion >= 80:
    print("Muy bien - B")
elif calificacion >= 70:
    print("Bien - C")
elif calificacion >= 60:
    print("Suficiente - D")
else:
    print("Reprobado - F")


# ========================================
# OPERADORES DE COMPARACIÓN
# ========================================

a = 10
b = 5

print("\n--- Operadores de comparación ---")
print("a =", a, "| b =", b)
print("a > b  (mayor que):", a > b)        # True
print("a < b  (menor que):", a < b)        # False
print("a >= b (mayor o igual):", a >= b)   # True
print("a <= b (menor o igual):", a <= b)   # False
print("a == b (igual a):", a == b)         # False
print("a != b (diferente de):", a != b)    # True


# ========================================
# OPERADORES LÓGICOS
# ========================================

edad = 20
tiene_licencia = True

# AND - Ambas condiciones deben ser verdaderas
if edad >= 18 and tiene_licencia:
    print("\nPuedes conducir")

# OR - Al menos una condición debe ser verdadera
es_fin_de_semana = True
es_feriado = False

if es_fin_de_semana or es_feriado:
    print("No hay clases")

# NOT - Invierte el valor
esta_lloviendo = False

if not esta_lloviendo:
    print("Puedes salir sin paraguas")


# ========================================
# CONDICIONALES ANIDADAS
# ========================================

edad = 25
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("\nPuedes comprar el videojuego")
    else:
        print("\nEres mayor de edad pero no tienes dinero")
else:
    print("\nEres menor de edad")


# ========================================
# EJERCICIO PRÁCTICO 1 - TAREA
# ========================================

"""
TAREA 4A: Detector de Números Pares e Impares

DESCRIPCIÓN:
Crea un programa que determine si un número es par o impar.

El programa debe:
1. Pedir un número al usuario
2. Verificar si es par o impar usando el operador módulo (%)
3. Mostrar el resultado

EJEMPLO DE EJECUCIÓN:
Ingresa un número: 8
El número es PAR

PISTA:
- Un número es par si el resto de dividirlo entre 2 es 0
- Usa: numero % 2 == 0
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 2 - TAREA
# ========================================

"""
TAREA 4B: Comparador de Dos Números

DESCRIPCIÓN:
Crea un programa que compare dos números y determine cuál es mayor.

El programa debe:
1. Pedir dos números al usuario
2. Comparar los números
3. Mostrar cuál es el mayor, o si son iguales

EJEMPLO DE EJECUCIÓN:
Primer número: 15
Segundo número: 10
El mayor es: 15

REQUISITOS:
- Usa if, elif y else
- Considera el caso cuando son iguales
"""

# Escribe tu código aquí:
