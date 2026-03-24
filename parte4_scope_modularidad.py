# ============================================================
#  HDT2 — Parte 4: Scope, Diseño Modular y Reutilización (20 pts)
#  CineData GT 2026 — Sistema de Análisis de Cines
# ============================================================

# ============================================================
#  Ejercicio 4.1 — Acumuladores con Scope Correcto  (6 pts)
# ============================================================
# CineData necesita procesar ventas y mantener estadísticas.
#
# Implementa `procesar_ventas(lista_ventas)` que reciba una lista de
# enteros y RETORNE un diccionario con estadísticas:
#   {
#     "total": suma,
#     "conteo": cantidad de elementos,
#     "promedio": promedio redondeado a 2 decimales,
#     "positivos": cantidad de valores > 0,
#     "mejor": valor máximo,
#     "peor": valor mínimo
#   }
#
# IMPORTANTE: todas las variables deben ser LOCALES a la función.
# NO uses variables globales. NO uses sum(), max(), min(), len().
#
# Implementa `comparar_periodos(ventas_actual, ventas_anterior)` que
# reciba dos listas y RETORNE un diccionario:
#   {
#     "total_actual": total del período actual,
#     "total_anterior": total del período anterior,
#     "diferencia": actual - anterior,
#     "cambio_pct": ((actual - anterior) / anterior) * 100, redondeado a 1 decimal,
#     "veredicto": "mejora" si cambio > 0, "declive" si < 0, "estable" si == 0
#   }
# DEBE usar procesar_ventas internamente.

def procesar_ventas(lista_ventas):
    total = 0
    conteo = 0
    positivos = 0
    mejor = None
    peor = None

    for venta in lista_ventas:
        total += venta
        conteo += 1

        if venta > 0:
            positivos += 1

        if mejor is None or venta > mejor:
            mejor = venta

        if peor is None or venta < peor:
            peor = venta

    if conteo == 0:
        promedio = 0
    else:
        promedio = round(total / conteo, 2)

    return {
        "total": total,
        "conteo": conteo,
        "promedio": promedio,
        "positivos": positivos,
        "mejor": mejor,
        "peor": peor,
    }


def comparar_periodos(ventas_actual, ventas_anterior):
    stats_actual = procesar_ventas(ventas_actual)
    stats_anterior = procesar_ventas(ventas_anterior)

    total_actual = stats_actual["total"]
    total_anterior = stats_anterior["total"]
    diferencia = total_actual - total_anterior

    if total_anterior == 0:
        if diferencia > 0:
            cambio_pct = 100.0
        else:
            cambio_pct = 0.0
    else:
        cambio_pct = round((diferencia / total_anterior) * 100, 1)

    if diferencia > 0:
        veredicto = "mejora"
    elif diferencia < 0:
        veredicto = "declive"
    else:
        veredicto = "estable"

    return {
        "total_actual": total_actual,
        "total_anterior": total_anterior,
        "diferencia": diferencia,
        "cambio_pct": cambio_pct,
        "veredicto": veredicto,
    }


# --- Pruebas (NO modificar) ---
print("=== Ejercicio 4.1 ===")
stats = procesar_ventas([120, 95, 110, 0, 200, 340, 290])
print(f"Stats: {stats}")

comp = comparar_periodos(
    [120, 135, 140, 155, 200, 310, 280],  # esta semana
    [100, 110, 105, 120, 180, 290, 250],  # semana pasada
)
print(f"Actual: {comp['total_actual']} | Anterior: {comp['total_anterior']}")
print(f"Diferencia: {comp['diferencia']} ({comp['cambio_pct']}%) → {comp['veredicto']}")

# Salida esperada:
# === Ejercicio 4.1 ===
# Stats: {'total': 1155, 'conteo': 7, 'promedio': 165.0, 'positivos': 6, 'mejor': 340, 'peor': 0}
# Actual: 1340 | Anterior: 1155
# Diferencia: 185 (16.0%) → mejora


# ============================================================
#  Ejercicio 4.2 — Funciones como Herramientas Reutilizables  (7 pts)
# ============================================================
# Implementa un mini-framework de análisis reutilizable:
#
# a) `aplicar_a_cada(funcion, lista)` — recibe una función y una lista.
#    Aplica la función a cada elemento y RETORNA una nueva lista con
#    los resultados. (Básicamente, implementar map() manualmente.)
#
# b) `filtrar(funcion, lista)` — recibe una función que retorna bool
#    y una lista. RETORNA una nueva lista solo con los elementos donde
#    la función retorna True. (Implementar filter() manualmente.)
#
# c) `reducir(funcion, lista, inicial)` — recibe una función de 2 args,
#    una lista y un valor inicial. Aplica la función acumulativamente:
#      resultado = inicial
#      para cada elemento: resultado = funcion(resultado, elemento)
#    RETORNA el resultado final. (Implementar reduce() manualmente.)
#
# SIN usar map(), filter(), functools.reduce() ni list comprehensions.

def aplicar_a_cada(funcion, lista):
    resultado = []
    for elemento in lista:
        resultado.append(funcion(elemento))
    return resultado


def filtrar(funcion, lista):
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado


def reducir(funcion, lista, inicial):
    acumulado = inicial
    for elemento in lista:
        acumulado = funcion(acumulado, elemento)
    return acumulado


# --- Funciones auxiliares para pruebas (NO modificar) ---
def doble(x):
    return x * 2

def es_mayor_100(x):
    return x > 100

def sumar(a, b):
    return a + b

def mayor(a, b):
    if a > b:
        return a
    return b


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 4.2 ===")
ventas = [120, 95, 340, 80, 200, 55, 180]

dobles = aplicar_a_cada(doble, ventas)
print(f"Dobles: {dobles}")

grandes = filtrar(es_mayor_100, ventas)
print(f"Mayores a 100: {grandes}")

total = reducir(sumar, ventas, 0)
print(f"Total (reducir): {total}")

maximo = reducir(mayor, ventas, 0)
print(f"Máximo (reducir): {maximo}")

# Salida esperada:
# === Ejercicio 4.2 ===
# Dobles: [240, 190, 680, 160, 400, 110, 360]
# Mayores a 100: [120, 340, 200, 180]
# Total (reducir): 1070
# Máximo (reducir): 340


# ============================================================
#  Ejercicio 4.3 — Pipeline de Análisis Modular  (7 pts)
# ============================================================
# Usando las funciones de 4.2 (aplicar_a_cada, filtrar, reducir) y
# las funciones auxiliares que tú definas, construye un pipeline.
#
# Implementa `analisis_completo(datos_salas)` que reciba un diccionario:
#   {nombre_sala: [ventas_diarias...]}
#
# El análisis debe:
# 1. Para cada sala, calcular el total (usa reducir con sumar)
# 2. Crear una lista de tuplas (nombre, total)
# 3. Filtrar solo salas con total > 1000 (define la función auxiliar necesaria)
# 4. De las salas filtradas, crear una lista con los totales y aplicar
#    doble para proyectar el mes (semana * 2 como estimación)
# 5. Calcular el gran total de proyecciones con reducir
#
# RETORNA un diccionario:
#   {
#     "resumen": lista de tuplas (nombre, total) de TODAS las salas,
#     "salas_fuertes": lista de nombres de salas con total > 1000,
#     "proyeccion_quincenal": lista de totales * 2 de las salas fuertes,
#     "gran_total_proyectado": suma de las proyecciones
#   }
#
# DEBES usar aplicar_a_cada, filtrar y/o reducir donde tenga sentido.
# Define las funciones auxiliares que necesites.

def analisis_completo(datos_salas):
    resumen = []
    for nombre_sala in datos_salas:
        ventas = datos_salas[nombre_sala]
        total_sala = reducir(sumar, ventas, 0)
        resumen.append((nombre_sala, total_sala))

    def sala_fuerte(par_sala_total):
        return par_sala_total[1] > 1000

    def solo_nombre(par_sala_total):
        return par_sala_total[0]

    def solo_total(par_sala_total):
        return par_sala_total[1]

    resumen_filtrado = filtrar(sala_fuerte, resumen)
    salas_fuertes = aplicar_a_cada(solo_nombre, resumen_filtrado)

    totales_fuertes = aplicar_a_cada(solo_total, resumen_filtrado)
    proyeccion_quincenal = aplicar_a_cada(doble, totales_fuertes)

    gran_total_proyectado = reducir(sumar, proyeccion_quincenal, 0)

    return {
        "resumen": resumen,
        "salas_fuertes": salas_fuertes,
        "proyeccion_quincenal": proyeccion_quincenal,
        "gran_total_proyectado": gran_total_proyectado,
    }


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 4.3 ===")
datos = {
    "IMAX":     [120, 135, 140, 155, 200, 310, 280],
    "Sala 3D":  [85, 70, 90, 88, 150, 260, 210],
    "Kids":     [60, 55, 65, 70, 95, 180, 150],
    "Premium":  [100, 80, 95, 105, 170, 300, 250],
}

resultado = analisis_completo(datos)
print("Resumen:")
for nombre, total in resultado["resumen"]:
    print(f"  {nombre:10s}: {total}")
print(f"Salas fuertes (>1000): {resultado['salas_fuertes']}")
print(f"Proyección quincenal: {resultado['proyeccion_quincenal']}")
print(f"Gran total proyectado: {resultado['gran_total_proyectado']}")

# Salida esperada:
# === Ejercicio 4.3 ===
# Resumen:
#   IMAX      : 1340
#   Sala 3D   : 953
#   Kids      : 675
#   Premium   : 1100
# Salas fuertes (>1000): ['IMAX', 'Premium']
# Proyección quincenal: [2680, 2200]
# Gran total proyectado: 4880
