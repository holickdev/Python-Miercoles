"""
===========================================
LECCIÓN 3: OPERACIONES MATEMÁTICAS
===========================================
Aprende a realizar cálculos en Python
"""

# ========================================
# OPERACIONES BÁSICAS
# ========================================

a = 10
b = 3

# SUMA (+)
suma = a + b
print("Suma:", a, "+", b, "=", suma)  # 13

# RESTA (-)
resta = a - b
print("Resta:", a, "-", b, "=", resta)  # 7

# MULTIPLICACIÓN (*)
multiplicacion = a * b
print("Multiplicación:", a, "*", b, "=", multiplicacion)  # 30

# DIVISIÓN (/)
division = a / b
print("División:", a, "/", b, "=", division)  # 3.333...


# ========================================
# OPERACIONES ESPECIALES
# ========================================

# DIVISIÓN ENTERA (//) - Resultado sin decimales
division_entera = a // b
print("\nDivisión entera:", a, "//", b, "=", division_entera)  # 3

# MÓDULO (%) - Resto de la división
modulo = a % b
print("Módulo (resto):", a, "%", b, "=", modulo)  # 1

# POTENCIA (**) - Elevar a una potencia
potencia = a ** b
print("Potencia:", a, "**", b, "=", potencia)  # 1000


# ========================================
# ORDEN DE OPERACIONES
# ========================================

# Python sigue el orden matemático: Paréntesis, Potencias, Multiplicación/División, Suma/Resta

resultado1 = 5 + 3 * 2
print("\n5 + 3 * 2 =", resultado1)  # 11 (primero multiplica, luego suma)

resultado2 = (5 + 3) * 2
print("(5 + 3) * 2 =", resultado2)  # 16 (primero suma, luego multiplica)


# ========================================
# OPERACIONES CON VARIABLES
# ========================================

precio = 100
descuento = 20

precio_final = precio - descuento
print("\nPrecio original:", precio)
print("Descuento:", descuento)
print("Precio final:", precio_final)


# ========================================
# INCREMENTAR Y DECREMENTAR
# ========================================

contador = 0
print("\nContador inicial:", contador)

contador = contador + 1  # Incrementar en 1
print("Después de +1:", contador)

contador = contador + 5  # Incrementar en 5
print("Después de +5:", contador)

contador = contador - 2  # Decrementar en 2
print("Después de -2:", contador)


# ========================================
# EJERCICIO PRÁCTICO - TAREA
# ========================================

"""
TAREA 3: Calculadora de Rectángulo

DESCRIPCIÓN:
Crea un programa que calcule el área y perímetro de un rectángulo.

El programa debe:
1. Pedir al usuario la base del rectángulo
2. Pedir al usuario la altura del rectángulo
3. Calcular el área (base × altura)
4. Calcular el perímetro (2 × (base + altura))
5. Mostrar ambos resultados

EJEMPLO DE EJECUCIÓN:
Ingresa la base del rectángulo: 5
Ingresa la altura del rectángulo: 3
El área es: 15
El perímetro es: 16

FÓRMULAS:
- Área = base × altura
- Perímetro = 2 × (base + altura)
"""

# Escribe tu código aquí:
