"""
===========================================
LECCIÓN 8: LISTAS - OPERACIONES
===========================================
Aprende a agregar, eliminar y manipular listas
"""

# ========================================
# AGREGAR ELEMENTOS
# ========================================

frutas = ["manzana", "banana"]
print("Lista inicial:", frutas)

# append() - Agregar al final
frutas.append("naranja")
print("Después de append:", frutas)

frutas.append("uva")
print("Después de otro append:", frutas)

# insert() - Agregar en una posición específica
frutas.insert(0, "fresa")  # Agregar al inicio
print("Después de insert en posición 0:", frutas)

frutas.insert(2, "kiwi")  # Agregar en posición 2
print("Después de insert en posición 2:", frutas)


# ========================================
# ELIMINAR ELEMENTOS
# ========================================

numeros = [10, 20, 30, 40, 50]
print("\nLista inicial:", numeros)

# pop() - Eliminar el último elemento
ultimo = numeros.pop()
print("Eliminado:", ultimo)
print("Lista después de pop:", numeros)

# pop(índice) - Eliminar en una posición específica
primero = numeros.pop(0)
print("Eliminado:", primero)
print("Lista después de pop(0):", numeros)

# remove() - Eliminar por valor
numeros.remove(30)
print("Después de remove(30):", numeros)


# ========================================
# OTRAS OPERACIONES ÚTILES
# ========================================

lista = [3, 1, 4, 1, 5, 9, 2, 6]
print("\nLista original:", lista)

# sort() - Ordenar de menor a mayor
lista.sort()
print("Ordenada:", lista)

# reverse() - Invertir el orden
lista.reverse()
print("Invertida:", lista)

# count() - Contar cuántas veces aparece un valor
numeros = [1, 2, 3, 2, 4, 2, 5]
veces = numeros.count(2)
print("\nEl número 2 aparece", veces, "veces")

# index() - Encontrar la posición de un valor
posicion = numeros.index(4)
print("El número 4 está en la posición:", posicion)


# ========================================
# COPIAR LISTAS
# ========================================

original = [1, 2, 3]
copia = original.copy()

copia.append(4)

print("\nOriginal:", original)
print("Copia:", copia)


# ========================================
# CONCATENAR LISTAS
# ========================================

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Unir con +
lista_completa = lista1 + lista2
print("\nLista concatenada:", lista_completa)

# Extender una lista con otra
lista1.extend(lista2)
print("Lista1 extendida:", lista1)


# ========================================
# EJERCICIO PRÁCTICO 1 - TAREA
# ========================================

"""
TAREA 8A: Gestor de Lista de Tareas

DESCRIPCIÓN:
Crea un programa que gestione una lista de tareas.

El programa debe:
1. Crear una lista vacía llamada "tareas"
2. Agregar tres tareas usando append():
   - "Estudiar Python"
   - "Hacer ejercicio"
   - "Leer un libro"
3. Mostrar la lista completa y el total de tareas
4. Completar (eliminar) la primera tarea usando pop(0)
5. Mostrar qué tarea se completó
6. Mostrar las tareas pendientes

EJEMPLO DE SALIDA:
Tareas: ['Estudiar Python', 'Hacer ejercicio', 'Leer un libro']
Total de tareas: 3
Tarea completada: Estudiar Python
Tareas pendientes: ['Hacer ejercicio', 'Leer un libro']

MÉTODOS A USAR:
- append() para agregar
- pop(0) para eliminar el primero
- len() para contar
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 2 - TAREA
# ========================================

"""
TAREA 8B: Análisis de Calificaciones

DESCRIPCIÓN:
Gestiona y analiza una lista de calificaciones.

Tienes esta lista inicial:
calificaciones = [75, 82, 90, 68, 85]

El programa debe:
1. Mostrar las calificaciones originales
2. Agregar una nueva calificación: 95
3. Mostrar la lista actualizada
4. Ordenar las calificaciones de menor a mayor
5. Mostrar la lista ordenada
6. Mostrar la peor calificación (primera después de ordenar)
7. Mostrar la mejor calificación (última después de ordenar)

EJEMPLO DE SALIDA:
Calificaciones originales: [75, 82, 90, 68, 85]
Después de agregar 95: [75, 82, 90, 68, 85, 95]
Ordenadas: [68, 75, 82, 85, 90, 95]
Peor calificación: 68
Mejor calificación: 95

MÉTODOS A USAR:
- append() para agregar
- sort() para ordenar
- Índices [0] y [-1] para acceder
"""

# Escribe tu código aquí:
