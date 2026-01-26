"""
===========================================
LECCIÓN 7: LISTAS - CONCEPTOS BÁSICOS
===========================================
Las listas guardan múltiples valores en una sola variable
"""

# ========================================
# CREAR UNA LISTA
# ========================================

# Lista de números
numeros = [5, 10, 15, 20, 25]
print("Lista de números:", numeros)

# Lista de textos
frutas = ["manzana", "banana", "naranja"]
print("Lista de frutas:", frutas)

# Lista mixta (no recomendado para principiantes)
mixta = [1, "hola", 3.14, True]
print("Lista mixta:", mixta)

# Lista vacía
lista_vacia = []
print("Lista vacía:", lista_vacia)


# ========================================
# ACCEDER A ELEMENTOS
# ========================================

# ¡IMPORTANTE! Las listas empiezan en 0, no en 1

frutas = ["manzana", "banana", "naranja", "uva", "pera"]

# Primer elemento (posición 0)
print("\nPrimer elemento:", frutas[0])  # manzana

# Segundo elemento (posición 1)
print("Segundo elemento:", frutas[1])  # banana

# Tercer elemento (posición 2)
print("Tercer elemento:", frutas[2])  # naranja


# ========================================
# ACCEDER DESDE EL FINAL
# ========================================

# Último elemento
print("\nÚltimo elemento:", frutas[-1])  # pera

# Penúltimo elemento
print("Penúltimo elemento:", frutas[-2])  # uva


# ========================================
# LONGITUD DE UNA LISTA
# ========================================

# len() nos dice cuántos elementos tiene la lista
cantidad = len(frutas)
print("\nLa lista tiene", cantidad, "elementos")

# Acceder al último elemento usando len()
ultimo = frutas[len(frutas) - 1]
print("Último elemento:", ultimo)


# ========================================
# MODIFICAR ELEMENTOS
# ========================================

print("\nLista original:", frutas)

# Cambiar el primer elemento
frutas[0] = "fresa"
print("Después de cambiar el primero:", frutas)

# Cambiar el último elemento
frutas[-1] = "sandía"
print("Después de cambiar el último:", frutas)


# ========================================
# EJERCICIO PRÁCTICO 1 - TAREA
# ========================================

"""
TAREA 7A: Explorador de Calificaciones

DESCRIPCIÓN:
Dada una lista de calificaciones, muestra información específica.

Tienes esta lista:
calificaciones = [85, 90, 78, 92, 88]

Debes mostrar:
1. La primera calificación
2. La última calificación
3. La calificación del medio (posición 2)
4. El total de calificaciones en la lista

EJEMPLO DE SALIDA:
Primera calificación: 85
Última calificación: 88
Calificación del medio: 78
Total de calificaciones: 5

PISTAS:
- Usa índices: [0], [-1], [2]
- Usa len() para contar elementos
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 2 - TAREA
# ========================================

"""
TAREA 7B: Modificador de Colores

DESCRIPCIÓN:
Modifica elementos específicos de una lista de colores.

Tienes esta lista:
colores = ["rojo", "azul", "verde", "amarillo"]

Debes:
1. Mostrar la lista original
2. Cambiar el segundo color (posición 1) a "morado"
3. Mostrar la lista modificada
4. Cambiar el último color a "negro"
5. Mostrar la lista final

EJEMPLO DE SALIDA:
Lista original: ['rojo', 'azul', 'verde', 'amarillo']
Lista modificada: ['rojo', 'morado', 'verde', 'amarillo']
Lista final: ['rojo', 'morado', 'verde', 'negro']

REQUISITOS:
- Usa índices para modificar elementos
- Muestra la lista después de cada cambio
"""

# Escribe tu código aquí:
