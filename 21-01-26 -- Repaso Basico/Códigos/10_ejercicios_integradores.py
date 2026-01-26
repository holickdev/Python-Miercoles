"""
===========================================
EJERCICIOS INTEGRADORES - TAREAS FINALES
===========================================
Estos ejercicios combinan todos los conceptos aprendidos
"""

# ========================================
# EJERCICIO 1: CALCULADORA DE PROMEDIO
# ========================================

"""
TAREA INTEGRADORA 1: Calculadora de Promedio de Calificaciones

DESCRIPCIÓN COMPLETA:
Crea un programa que calcule el promedio de calificaciones y determine
si el estudiante aprobó o reprobó.

PASOS DETALLADOS:

1. ENTRADA DE DATOS:
   - Pedir al usuario cuántas calificaciones va a ingresar
   - Crear una lista vacía llamada "calificaciones"
   
2. RECOLECTAR CALIFICACIONES:
   - Usar un ciclo for para pedir cada calificación
   - Agregar cada calificación a la lista con append()
   - Mostrar el número de calificación (1, 2, 3, etc.)
   
3. CALCULAR EL PROMEDIO:
   - Crear una variable suma = 0
   - Recorrer la lista con otro ciclo for
   - Sumar todas las calificaciones
   - Dividir la suma entre la cantidad de calificaciones
   
4. MOSTRAR RESULTADOS:
   - Mostrar la lista completa de calificaciones
   - Mostrar el promedio calculado
   - Si el promedio es >= 70, mostrar "¡Aprobado!"
   - Si el promedio es < 70, mostrar "Reprobado"

EJEMPLO DE EJECUCIÓN:
¿Cuántas calificaciones vas a ingresar? 4
Calificación 1: 85
Calificación 2: 90
Calificación 3: 78
Calificación 4: 92

Calificaciones: [85, 90, 78, 92]
Promedio: 86.25
¡Aprobado!

CONCEPTOS QUE USARÁS:
- input() y int()
- Listas y append()
- Ciclo for con range()
- Operaciones matemáticas
- Condicionales if/else
- len() para contar elementos
"""

# Escribe tu código aquí:




# ========================================
# EJERCICIO 2: SEPARADOR DE PARES E IMPARES
# ========================================

"""
TAREA INTEGRADORA 2: Clasificador de Números Pares e Impares

DESCRIPCIÓN COMPLETA:
Crea un programa que separe una lista de números en dos listas:
una con números pares y otra con números impares.

PASOS DETALLADOS:

1. DATOS INICIALES:
   - Tienes esta lista: numeros = [12, 7, 23, 8, 15, 4, 19, 6]
   - Crear dos listas vacías: pares = [] e impares = []
   
2. CLASIFICAR NÚMEROS:
   - Recorrer la lista original con un ciclo for
   - Para cada número, verificar si es par o impar
   - Si es par (numero % 2 == 0), agregarlo a la lista "pares"
   - Si es impar, agregarlo a la lista "impares"
   
3. MOSTRAR RESULTADOS:
   - Mostrar la lista original
   - Mostrar la lista de números pares
   - Mostrar la lista de números impares

EJEMPLO DE SALIDA:
Lista original: [12, 7, 23, 8, 15, 4, 19, 6]
Números pares: [12, 8, 4, 6]
Números impares: [7, 23, 15, 19]

CONCEPTOS QUE USARÁS:
- Listas múltiples
- Ciclo for con range(len())
- Operador módulo (%)
- Condicionales if/else
- append() para agregar a listas
"""

# Escribe tu código aquí:




# ========================================
# EJERCICIO 3: BUSCAR Y REEMPLAZAR
# ========================================

"""
TAREA INTEGRADORA 3: Buscador y Reemplazador de Valores

DESCRIPCIÓN COMPLETA:
Crea un programa que busque todas las apariciones de un número
en una lista y las reemplace por otro número.

PASOS DETALLADOS:

1. DATOS INICIALES:
   - Tienes esta lista: numeros = [10, 20, 30, 20, 40, 20, 50]
   - Definir qué número buscar (por ejemplo, 20)
   - Definir por qué número reemplazar (por ejemplo, 99)
   
2. MOSTRAR LISTA ORIGINAL:
   - Imprimir la lista antes de hacer cambios
   
3. BUSCAR Y REEMPLAZAR:
   - Recorrer la lista con un ciclo for usando índices
   - Para cada elemento, verificar si es igual al número buscado
   - Si es igual, reemplazarlo con el nuevo número
   - Usar: numeros[i] = reemplazar
   
4. MOSTRAR RESULTADO:
   - Imprimir la lista modificada

EJEMPLO DE SALIDA:
Lista original: [10, 20, 30, 20, 40, 20, 50]
Lista modificada: [10, 99, 30, 99, 40, 99, 50]

CONCEPTOS QUE USARÁS:
- Listas y modificación de elementos
- Ciclo for con range(len())
- Condicionales if
- Acceso por índice
"""

# Escribe tu código aquí:




# ========================================
# EJERCICIO 4: CALCULADORA DE ESTADÍSTICAS
# ========================================

"""
TAREA INTEGRADORA 4: Calculadora de Estadísticas Completa

DESCRIPCIÓN COMPLETA:
Crea un programa que calcule estadísticas completas de una lista de números.

PASOS DETALLADOS:

1. DATOS INICIALES:
   - Tienes esta lista: numeros = [45, 23, 67, 12, 89, 34, 56, 78]
   
2. CALCULAR LA SUMA:
   - Crear variable suma = 0
   - Recorrer la lista sumando todos los elementos
   
3. CALCULAR EL PROMEDIO:
   - Dividir la suma entre la cantidad de elementos
   - Usar len(numeros) para obtener la cantidad
   
4. ENCONTRAR EL MAYOR:
   - Crear variable mayor = numeros[0]
   - Recorrer la lista comparando cada número
   - Si encuentras uno mayor, actualizar la variable
   
5. ENCONTRAR EL MENOR:
   - Crear variable menor = numeros[0]
   - Recorrer la lista comparando cada número
   - Si encuentras uno menor, actualizar la variable
   
6. MOSTRAR TODOS LOS RESULTADOS:
   - Lista original
   - Cantidad de elementos
   - Suma total
   - Promedio
   - Número mayor
   - Número menor

EJEMPLO DE SALIDA:
Lista: [45, 23, 67, 12, 89, 34, 56, 78]
Cantidad de elementos: 8
Suma total: 404
Promedio: 50.5
Número mayor: 89
Número menor: 12

CONCEPTOS QUE USARÁS:
- Listas
- Ciclos for
- Variables acumuladoras
- Operaciones matemáticas
- Comparaciones
- len() para contar
"""

# Escribe tu código aquí:




# ========================================
# EJERCICIO 5: SISTEMA DE LISTA DE COMPRAS
# ========================================

"""
TAREA INTEGRADORA 5: Sistema de Lista de Compras Interactivo

DESCRIPCIÓN COMPLETA:
Crea un programa interactivo que gestione una lista de compras
con productos y precios.

PASOS DETALLADOS:

1. PREPARACIÓN:
   - Crear dos listas vacías: productos = [] y precios = []
   
2. CREAR EL MENÚ:
   - Usar un ciclo while True para mantener el programa activo
   - Mostrar 4 opciones:
     1. Agregar producto
     2. Ver lista
     3. Calcular total
     4. Salir
   
3. OPCIÓN 1 - AGREGAR PRODUCTO:
   - Pedir el nombre del producto
   - Pedir el precio (usar float() para decimales)
   - Agregar el nombre a la lista "productos"
   - Agregar el precio a la lista "precios"
   - Mostrar mensaje de confirmación
   
4. OPCIÓN 2 - VER LISTA:
   - Recorrer ambas listas con un ciclo for
   - Mostrar cada producto con su precio
   - Formato: "1. Manzanas - $2.50"
   - Usar range(len(productos))
   
5. OPCIÓN 3 - CALCULAR TOTAL:
   - Crear variable total = 0
   - Recorrer la lista de precios
   - Sumar todos los precios
   - Mostrar el total a pagar
   
6. OPCIÓN 4 - SALIR:
   - Mostrar mensaje de despedida
   - Usar break para salir del ciclo while
   
7. VALIDACIÓN:
   - Si el usuario elige una opción inválida, mostrar error

EJEMPLO DE EJECUCIÓN:
1. Agregar producto
2. Ver lista
3. Calcular total
4. Salir
Elige una opción: 1
Nombre del producto: Manzanas
Precio: 2.50
¡Producto agregado!

1. Agregar producto
2. Ver lista
3. Calcular total
4. Salir
Elige una opción: 2

--- LISTA DE COMPRAS ---
1. Manzanas - $2.5

CONCEPTOS QUE USARÁS:
- Dos listas paralelas (productos y precios)
- Ciclo while True
- Menú con if/elif/else
- input() para texto y números
- float() para decimales
- Ciclos for para recorrer listas
- break para salir del ciclo
"""

# Escribe tu código aquí:




# ========================================
# EJERCICIO 6: JUEGO DE ADIVINANZAS MÚLTIPLES
# ========================================

"""
TAREA INTEGRADORA 6: Juego de Adivinar Múltiples Números

DESCRIPCIÓN COMPLETA:
Crea un juego donde el usuario debe adivinar varios números secretos.

PASOS DETALLADOS:

1. CONFIGURACIÓN INICIAL:
   - Crear lista de números secretos: numeros_secretos = [7, 3, 9, 5]
   - Crear lista vacía para números adivinados: adivinados = []
   - Crear contador de intentos: intentos = 0
   - Mostrar instrucciones al jugador
   
2. CICLO PRINCIPAL:
   - Usar while len(adivinados) < 4
   - Mientras no haya adivinado los 4 números, continuar
   
3. PEDIR INTENTO:
   - Pedir al usuario que adivine un número (1-10)
   - Incrementar el contador de intentos
   
4. VERIFICAR EL NÚMERO:
   - Crear variable encontrado = False
   - Recorrer la lista de números secretos con un ciclo for
   - Si el número está en numeros_secretos:
     a. Verificar si ya fue adivinado antes
     b. Si NO está en "adivinados":
        - Agregarlo a la lista "adivinados"
        - Mostrar mensaje de éxito
        - Mostrar cuántos lleva adivinados
        - Cambiar encontrado a True
        - Salir del ciclo con break
     c. Si YA está en "adivinados":
        - Mostrar que ya lo había adivinado
        - Cambiar encontrado a True
        - Salir del ciclo con break
   
5. SI NO LO ENCONTRÓ:
   - Si encontrado es False, mostrar "Incorrecto, intenta de nuevo"
   
6. CUANDO TERMINE:
   - Mostrar mensaje de felicitación
   - Mostrar total de intentos
   - Mostrar cuáles eran los números secretos

EJEMPLO DE EJECUCIÓN:
Debes adivinar 4 números entre 1 y 10

Intenta adivinar un número: 5
Incorrecto, intenta de nuevo

Intenta adivinar un número: 7
¡Correcto! Has adivinado 1 de 4

Intenta adivinar un número: 7
Ya habías adivinado ese número

Intenta adivinar un número: 3
¡Correcto! Has adivinado 2 de 4

... (continúa hasta adivinar los 4)

¡Felicidades! Adivinaste todos en 8 intentos
Los números eran: [7, 3, 9, 5]

CONCEPTOS QUE USARÁS:
- Dos listas (secretos y adivinados)
- Ciclo while con condición
- Ciclo for anidado
- Condicionales múltiples
- Operador "in" para verificar si está en lista
- len() para contar elementos
- break para salir de ciclos
- Variables booleanas (True/False)
"""

# Escribe tu código aquí:
