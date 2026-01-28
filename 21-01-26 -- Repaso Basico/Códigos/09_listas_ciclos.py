"""
===========================================
LECCIÓN 9: LISTAS Y CICLOS
===========================================
Aprende a recorrer listas con ciclos for
"""

# ========================================
# RECORRER UNA LISTA UTITLIZANDO FOR
# ========================================

frutas = ["manzana", "banana", "naranja", "uva"]

# Forma 1: Recorrer por índices
print("--- Recorriendo por índices ---")
for i in range(len(frutas)):
    print("Posición", i, ":", frutas[i])


# ========================================
# USAR LISTAS CON CICLOS
# ========================================

# Ejemplo: Mostrar números y sus cuadrados
numeros = [1, 2, 3, 4, 5]

print("\n--- Números y sus cuadrados ---")
for i in range(len(numeros)):
    cuadrado = numeros[i] ** 2
    print(numeros[i], "al cuadrado es", cuadrado)


# ========================================
# CREAR LISTAS CON CICLOS
# ========================================

# Crear una lista de números pares
pares = []
for i in range(0, 11, 2):
    pares.append(i)

print("\nNúmeros pares:", pares)

# Crear una lista de cuadrados
cuadrados = []
for i in range(1, 6):
    cuadrados.append(i ** 2)

print("Cuadrados:", cuadrados)


# ========================================
# BUSCAR EN UNA LISTA
# ========================================

calificaciones = [85, 90, 78, 92, 88, 76, 95]

# Buscar calificaciones mayores a 90
print("\n--- Calificaciones mayores a 90 ---")
for i in range(len(calificaciones)):
    if calificaciones[i] > 90:
        print("Estudiante", i + 1, ":", calificaciones[i])


# ========================================
# CALCULAR CON LISTAS
# ========================================

numeros = [10, 20, 30, 40, 50]

# Calcular la suma
suma = 0
for i in range(len(numeros)):
    suma = suma + numeros[i]

print("\nSuma total:", suma)

# Calcular el promedio
promedio = suma / len(numeros)
print("Promedio:", promedio)


# ========================================
# ENCONTRAR EL MAYOR Y MENOR
# ========================================

numeros = [45, 23, 67, 12, 89, 34]

# Encontrar el mayor
mayor = numeros[0]  # Asumimos que el primero es el mayor
for i in range(len(numeros)):
    if numeros[i] > mayor:
        mayor = numeros[i]

print("\nEl número mayor es:", mayor)

# Encontrar el menor
menor = numeros[0]  # Asumimos que el primero es el menor
for i in range(len(numeros)):
    if numeros[i] < menor:
        menor = numeros[i]

print("El número menor es:", menor)


# ========================================
# MODIFICAR ELEMENTOS CON CICLOS
# ========================================

# Duplicar todos los números
numeros = [1, 2, 3, 4, 5]
print("\nLista original:", numeros)

for i in range(len(numeros)):
    numeros[i] = numeros[i] * 2

print("Lista duplicada:", numeros)


# ========================================
# EJERCICIO PRÁCTICO 1 - TAREA
# ========================================

"""
TAREA 9A: Contador de Positivos y Negativos

DESCRIPCIÓN:
Cuenta cuántos números positivos y negativos hay en una lista.

Tienes esta lista:
numeros = [5, -3, 8, -1, 0, 12, -7, 4]

El programa debe:
1. Crear dos contadores: positivos = 0 y negativos = 0
2. Recorrer la lista con un ciclo for usando range(len(numeros))
3. Por cada número:
   - Si es mayor que 0, incrementar positivos
   - Si es menor que 0, incrementar negativos
4. Mostrar el total de positivos y negativos

EJEMPLO DE SALIDA:
Números positivos: 4
Números negativos: 3

PISTAS:
- Usa if numeros[i] > 0 para positivos
- Usa elif numeros[i] < 0 para negativos
- El 0 no se cuenta como positivo ni negativo
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 2 - TAREA
# ========================================

"""
TAREA 9B: Generador de Múltiplos

DESCRIPCIÓN:
Crea una lista con los primeros 10 múltiplos de 3.

El programa debe:
1. Crear una lista vacía llamada "multiplos"
2. Usar un ciclo for con range(1, 11)
3. En cada iteración, calcular 3 * i
4. Agregar el resultado a la lista con append()
5. Mostrar la lista final

EJEMPLO DE SALIDA:
Múltiplos de 3: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

REQUISITOS:
- La lista debe tener exactamente 10 elementos
- Usa append() para agregar cada múltiplo
"""

# Escribe tu código aquí:


# ========================================
# EJERCICIO PRÁCTICO 3 - TAREA
# ========================================

"""
TAREA 9C: Buscador de Números

DESCRIPCIÓN:
Busca un número específico en una lista y muestra su posición.

Tienes esta lista:
numeros = [10, 25, 30, 45, 50, 60]

El programa debe:
1. Definir qué número buscar (por ejemplo, 30)
2. Crear variables: encontrado = False y posicion = -1
3. Recorrer la lista con un ciclo for
4. Si encuentra el número:
   - Cambiar encontrado a True
   - Guardar la posición (i)
   - Salir del ciclo con break
5. Después del ciclo, mostrar si lo encontró y en qué posición

EJEMPLO DE SALIDA (si encuentra):
El número 30 está en la posición 2

EJEMPLO DE SALIDA (si no encuentra):
El número 100 no está en la lista

PISTAS:
- Usa if numeros[i] == buscar
- Usa break para salir del ciclo cuando encuentres el número
"""

# Escribe tu código aquí:
