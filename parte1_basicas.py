# ============================================================
#  HDT2 — Parte 1: Funciones Básicas, Parámetros y Return (20 pts)
#  CineData GT 2026 — Sistema de Análisis de Cines
# ============================================================

# ============================================================
#  Ejercicio 1.1 — Precio con Descuento  (4 pts)
# ============================================================
# Implementa `precio_con_descuento(precio_base, porcentaje)` que:
#   - Reciba el precio base (float) y el porcentaje de descuento (float)
#   - RETORNE el precio final después de aplicar el descuento
#   - El porcentaje viene como número entero (ej: 15 = 15%)
#
# Luego implementa `precio_con_iva(precio, iva)` que:
#   - Reciba un precio (float) y el porcentaje de IVA (float)
#   - RETORNE el precio con IVA incluido
#
# Ambas funciones deben redondear a 2 decimales con round().

def precio_con_descuento(precio_base, porcentaje):
    descuento = precio_base * (porcentaje / 100)
    return round(precio_base - descuento, 2)


def precio_con_iva(precio, iva):
    iva_amount = precio * (iva / 100)
    return round(precio + iva_amount, 2)


# --- Pruebas (NO modificar) ---
print("=== Ejercicio 1.1 ===")
print(f"Q100 - 25% = Q{precio_con_descuento(100.0, 25)}")
print(f"Q85 - 10% = Q{precio_con_descuento(85.0, 10)}")
print(f"Q76.5 + 12% IVA = Q{precio_con_iva(76.5, 12)}")
print(f"Q200 + 12% IVA = Q{precio_con_iva(200.0, 12)}")

# Salida esperada:
# === Ejercicio 1.1 ===
# Q100 - 25% = Q75.0
# Q85 - 10% = Q76.5
# Q76.5 + 12% IVA = Q85.68
# Q200 + 12% IVA = Q224.0


# ============================================================
#  Ejercicio 1.2 — Clasificador de Películas  (5 pts)
# ============================================================
# Implementa `clasificar_duracion(minutos)` que RETORNE:
#   - "corta"    si < 90 minutos
#   - "estándar" si 90 a 150 minutos (inclusive)
#   - "larga"    si > 150 minutos
#
# Implementa `clasificar_rating(rating)` que RETORNE:
#   - "mala"      si < 4.0
#   - "regular"   si 4.0 a 6.9 (inclusive)
#   - "buena"     si 7.0 a 8.4 (inclusive)
#   - "excelente" si >= 8.5
#
# Implementa `es_recomendada(duracion, rating)` que RETORNE True
# si la película es "buena" o "excelente" Y su duración es "estándar" o "corta".
# DEBE usar las dos funciones anteriores internamente.

def clasificar_duracion(minutos):
    if minutos < 90:
        return "corta"
    elif minutos <= 150:
        return "estándar"
    else:
        return "larga"


def clasificar_rating(rating):
    if rating < 4.0:
        return "mala"
    elif rating <= 6.9:
        return "regular"
    elif rating <= 8.4:
        return "buena"
    else:
        return "excelente"


def es_recomendada(duracion, rating):
    duracion_clase = clasificar_duracion(duracion)
    rating_clase = clasificar_rating(rating)
    return (rating_clase in ["buena", "excelente"]) and (duracion_clase in ["estándar", "corta"])


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 1.2 ===")
peliculas = [
    ("Dune: Parte 3", 175, 8.7),
    ("Inside Out 3", 105, 8.9),
    ("Película Mala", 85, 3.2),
    ("Drama Largo", 200, 7.5),
    ("Comedia OK", 95, 6.0),
]
for titulo, dur, rat in peliculas:
    d = clasificar_duracion(dur)
    r = clasificar_rating(rat)
    rec = "Sí" if es_recomendada(dur, rat) else "No"
    print(f"  {titulo:20s} | {d:10s} | {r:10s} | Recomendada: {rec}")

# Salida esperada:
# === Ejercicio 1.2 ===
#   Dune: Parte 3        | larga      | excelente  | Recomendada: No
#   Inside Out 3          | estándar   | excelente  | Recomendada: Sí
#   Película Mala         | corta      | mala       | Recomendada: No
#   Drama Largo           | larga      | buena      | Recomendada: No
#   Comedia OK            | estándar   | regular    | Recomendada: No


# ============================================================
#  Ejercicio 1.3 — Retorno Múltiple: Análisis de Fila  (5 pts)
# ============================================================
# Implementa `analizar_ventas(ventas)` que reciba una lista de enteros
# (ventas diarias) y RETORNE una tupla con 4 valores:
#   (total, promedio, mejor_dia, peor_dia)
#
# Donde:
#   - total: suma de todas las ventas
#   - promedio: promedio redondeado a 2 decimales
#   - mejor_dia: índice (0-based) del día con más ventas
#   - peor_dia: índice (0-based) del día con menos ventas
#
# SIN usar sum(), max(), min(), len(). Usa ciclos for para todo.

def analizar_ventas(ventas):
    total = 0
    mejor_dia = 0
    peor_dia = 0
    for i in range(0, len(ventas)):
        total = total + ventas[i]
        if ventas[i] > ventas[mejor_dia]:
            mejor_dia = i
        if ventas[i] < ventas[peor_dia]:
            peor_dia = i
    promedio = round(total / len(ventas), 2)
    return (total, promedio, mejor_dia, peor_dia)


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 1.3 ===")
semana_imax = [120, 95, 110, 130, 200, 340, 290]
dias = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

total, prom, mejor, peor = analizar_ventas(semana_imax)
print(f"Total: {total}")
print(f"Promedio: {prom}")
print(f"Mejor día: {dias[mejor]} ({semana_imax[mejor]} entradas)")
print(f"Peor día: {dias[peor]} ({semana_imax[peor]} entradas)")

# Salida esperada:
# === Ejercicio 1.3 ===
# Total: 1285
# Promedio: 183.57
# Mejor día: Sáb (340 entradas)
# Peor día: Mar (95 entradas)


# ============================================================
#  Ejercicio 1.4 — Formato de Reportes  (6 pts)
# ============================================================
# Implementa `formato_moneda(cantidad)` que RETORNE un string
# con formato "Q1,234.56" (con coma de miles y 2 decimales).
#   Tip: puedes usar f"{cantidad:,.2f}" y reemplazar caracteres,
#   o construirlo manualmente.
#
# Implementa `barra_visual(valor, maximo, ancho=20)` que RETORNE un
# string de barra proporcional. Ejemplo con valor=75, maximo=100, ancho=20:
#   "███████████████░░░░░ 75%"
# Donde:
#   - proporcion = valor / maximo
#   - llenos = round(proporcion * ancho)
#   - vacíos = ancho - llenos
#   - Usa "█" para lleno y "░" para vacío
#   - Al final muestra el porcentaje redondeado a 0 decimales
#
# Implementa `linea_reporte(nombre, valor, maximo, ancho=20)` que RETORNE:
#   "Sala IMAX   | Q1,285.00 | ███████████████░░░░░ 75%"
# Usa formato_moneda y barra_visual internamente.
# El nombre debe ocupar 14 caracteres alineado a la izquierda.

def formato_moneda(cantidad):
    formatted = f"{cantidad:,.2f}"
    return "Q" + formatted


def barra_visual(valor, maximo, ancho=20):
    proporcion = valor / maximo
    llenos = round(proporcion * ancho)
    vacios = ancho - llenos
    barra = "█" * llenos + "░" * vacios
    porcentaje = round(proporcion * 100)
    return f"{barra} {porcentaje}%"


def linea_reporte(nombre, valor, maximo, ancho=20):
    nombre_formateado = f"{nombre:<14}"
    moneda = formato_moneda(valor)
    barra = barra_visual(valor, maximo, ancho)
    return f"{nombre_formateado} | {moneda:>11} | {barra}"


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 1.4 ===")
print(f"Moneda: {formato_moneda(29250.0)}")
print(f"Moneda: {formato_moneda(850.5)}")
print(f"Barra:  {barra_visual(75, 100)}")
print(f"Barra:  {barra_visual(340, 400, 10)}")
print()

salas_data = [("Sala IMAX", 1285), ("Sala 3D", 953), ("Sala Kids", 675), ("Sala Premium", 1100)]
maximo = 1285
for nombre, valor in salas_data:
    print(linea_reporte(nombre, valor, maximo))

# Salida esperada:
# === Ejercicio 1.4 ===
# Moneda: Q29,250.00
# Moneda: Q850.50
# Barra:  ███████████████░░░░░ 75%
# Barra:  █████████░ 85%
#
# Sala IMAX      | Q1,285.00  | ████████████████████ 100%
# Sala 3D        | Q953.00    | ███████████████░░░░░ 74%
# Sala Kids      | Q675.00    | ███████████░░░░░░░░░ 53%
# Sala Premium   | Q1,100.00  | █████████████████░░░ 86%
