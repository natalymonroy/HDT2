# ============================================================
#  HDT2 — Parte 2: Parámetros Default y Keyword Args  (20 pts)
#  CineData GT 2026 — Sistema de Análisis de Cines
# ============================================================

# ============================================================
#  Ejercicio 2.1 — Calculadora de Ingresos Flexible  (7 pts)
# ============================================================
# Implementa `calcular_ingreso` que reciba:
#   - precio_base (float)
#   - vendidas (int)
#   - descuento (float, default=0.0): porcentaje de descuento
#   - iva (float, default=12.0): porcentaje de IVA
#   - propina_pct (float, default=0.0): porcentaje de propina opcional
#
# Proceso:
#   1. ingreso_bruto = precio_base * vendidas
#   2. monto_descuento = ingreso_bruto * (descuento / 100)
#   3. subtotal = ingreso_bruto - monto_descuento
#   4. monto_iva = subtotal * (iva / 100)
#   5. monto_propina = subtotal * (propina_pct / 100)
#   6. total = subtotal + monto_iva + monto_propina
#
# RETORNA una tupla:
#   (ingreso_bruto, monto_descuento, subtotal, monto_iva, monto_propina, total)
# Todos los valores redondeados a 2 decimales.

def calcular_ingreso(precio_base, vendidas, descuento=0.0, iva=12.0, propina_pct=0.0):
    ingreso_bruto = precio_base * vendidas
    monto_descuento = ingreso_bruto * (descuento / 100)
    subtotal = ingreso_bruto - monto_descuento
    monto_iva = subtotal * (iva / 100)
    monto_propina = subtotal * (propina_pct / 100)
    total = subtotal + monto_iva + monto_propina
    
    return (
        round(ingreso_bruto, 2),
        round(monto_descuento, 2),
        round(subtotal, 2),
        round(monto_iva, 2),
        round(monto_propina, 2),
        round(total, 2)
    )


# --- Pruebas (NO modificar) ---
if __name__ == "__main__":
    print("=== Ejercicio 2.1 ===")

    # Caso 1: solo precio y vendidas (usa defaults)
    r1 = calcular_ingreso(85.0, 100)
    print(f"Caso 1 — Bruto: Q{r1[0]} | Desc: Q{r1[1]} | Sub: Q{r1[2]} | IVA: Q{r1[3]} | Prop: Q{r1[4]} | Total: Q{r1[5]}")

    # Caso 2: con descuento usando keyword arg
    r2 = calcular_ingreso(85.0, 100, descuento=15.0)
    print(f"Caso 2 — Bruto: Q{r2[0]} | Desc: Q{r2[1]} | Sub: Q{r2[2]} | IVA: Q{r2[3]} | Prop: Q{r2[4]} | Total: Q{r2[5]}")

    # Caso 3: sin IVA (evento exento) con propina
    r3 = calcular_ingreso(50.0, 200, iva=0.0, propina_pct=10.0)
    print(f"Caso 3 — Bruto: Q{r3[0]} | Desc: Q{r3[1]} | Sub: Q{r3[2]} | IVA: Q{r3[3]} | Prop: Q{r3[4]} | Total: Q{r3[5]}")

    # Salida esperada:
    # === Ejercicio 2.1 ===
    # Caso 1 — Bruto: Q8500.0 | Desc: Q0.0 | Sub: Q8500.0 | IVA: Q1020.0 | Prop: Q0.0 | Total: Q9520.0
    # Caso 2 — Bruto: Q8500.0 | Desc: Q1275.0 | Sub: Q7225.0 | IVA: Q867.0 | Prop: Q0.0 | Total: Q8092.0
    # Caso 3 — Bruto: Q10000.0 | Desc: Q0.0 | Sub: Q10000.0 | IVA: Q0.0 | Prop: Q1000.0 | Total: Q11000.0


# ============================================================
#  Ejercicio 2.2 — Generador de Credenciales  (6 pts)
# ============================================================
# Implementa `generar_credencial` que reciba:
#   - nombre_completo (str): ej. "Carlos Andrés Mendoza"
#   - zona (str, default="general")
#   - numero (int, default=1)
#   - prefijo (str, default="CD26")
#
# RETORNA un string con formato: "[PREFIJO]-[ZONA3]-[INICIALES][NUMERO]"
# Donde:
#   - ZONA3: primeras 3 letras de la zona en MAYÚSCULAS
#   - INICIALES: primera letra del primer nombre + primera letra del
#     último apellido, en MAYÚSCULAS
#   - NUMERO: con 4 dígitos rellenados con ceros (usa zfill)
#
# Ejemplo: generar_credencial("Carlos Mendoza", zona="vip", numero=47)
#          → "CD26-VIP-CM0047"

def generar_credencial(nombre_completo, zona="general", numero=1, prefijo="CD26"):
    # Obtener iniciales: primera letra del primer nombre + primera letra del último apellido
    palabras = nombre_completo.split()
    iniciales = palabras[0][0] + palabras[-1][0]
    iniciales = iniciales.upper()
    
    # Primeras 3 letras de la zona en MAYÚSCULAS
    zona3 = zona[:3].upper()
    
    # Número con 4 dígitos
    numero_formateado = str(numero).zfill(4)
    
    return f"{prefijo}-{zona3}-{iniciales}{numero_formateado}"


# --- Pruebas (NO modificar) ---
if __name__ == "__main__":
    print("\n=== Ejercicio 2.2 ===")
    print(generar_credencial("Carlos Mendoza", zona="vip", numero=47))
    print(generar_credencial("Ana García", numero=5))
    print(generar_credencial("José Roberto López", zona="preferencia", numero=312))
    print(generar_credencial("María Luisa Fernández Torres", zona="imax", numero=88, prefijo="FE26"))

    # Salida esperada:
    # === Ejercicio 2.2 ===
    # CD26-VIP-CM0047
    # CD26-GEN-AG0005
    # CD26-PRE-JL0312
    # FE26-IMA-MT0088


# ============================================================
#  Ejercicio 2.3 — Constructor de Reportes Configurable  (7 pts)
# ============================================================
# Implementa `construir_reporte` que reciba:
#   - titulo (str): título del reporte
#   - datos (list): lista de tuplas (nombre, valor)
#   - moneda (str, default="Q"): símbolo de moneda
#   - mostrar_promedio (bool, default=True): si incluir promedio al final
#   - mostrar_ranking (bool, default=False): si numerar las filas (#1, #2...)
#   - ancho_nombre (int, default=20): ancho del campo nombre
#
# RETORNA un string multilínea con:
#   - Línea de título centrada en 40 caracteres con "=" a los lados
#   - Cada fila formateada con nombre (alineado izquierda) y valor con moneda
#   - Si mostrar_ranking=True, prefijo "#N " antes del nombre
#   - Una línea separadora "---"
#   - Si mostrar_promedio=True, una línea final con el promedio
#
# Para el promedio: calcula con for, SIN usar sum() ni len().

def construir_reporte(titulo, datos, moneda="Q", mostrar_promedio=True,
                      mostrar_ranking=False, ancho_nombre=20):
    # Crear línea de título centrada
    linea_titulo = f" {titulo} "
    padding_total = 40 - len(linea_titulo)
    padding_left = padding_total // 2
    padding_right = padding_total - padding_left
    titulo_formateado = "=" * padding_left + linea_titulo + "=" * padding_right
    
    lineas = [titulo_formateado]
    
    # Procesar cada fila de datos
    total = 0
    contador = 0
    for nombre, valor in datos:
        contador += 1
        total += valor
        
        # Formatear valor con moneda y separador de miles
        valor_formateado = f"{valor:,.2f}".replace(",", "." if moneda == "$" else ",")
        valor_formateado = f"{valor_formateado}".replace(".", ",") if moneda == "Q" else valor_formateado
        
        # Usar formato correcto de separador de miles
        valor_formateado = f"{valor:,}".replace(",", "_TEMP_")
        valor_formateado = valor_formateado.replace("_TEMP_", ".")
        valor_formateado = f"{valor:,.2f}"
        if moneda == "Q":
            valor_formateado = valor_formateado.replace(",", "_")
            valor_formateado = valor_formateado.replace(".", ",")
            valor_formateado = valor_formateado.replace("_", ".")
        
        # Simpler approach
        partes = f"{valor:.2f}".split(".")
        entero = partes[0]
        decimales = partes[1]
        
        # Agregar separadores de miles
        entero_separado = ""
        for i, digito in enumerate(reversed(entero)):
            if i > 0 and i % 3 == 0:
                entero_separado = "." + entero_separado
            entero_separado = digito + entero_separado
        
        valor_formateado = f"{entero_separado},{decimales}"
        
        # Prefijo de ranking si aplica
        prefijo = f"#{contador} " if mostrar_ranking else ""
        
        # Alinear nombre a la izquierda
        nombre_alineado = (prefijo + nombre).ljust(ancho_nombre + (5 if mostrar_ranking else 0))
        
        lineas.append(f"{nombre_alineado} {moneda}{valor_formateado}")
    
    # Línea separadora
    lineas.append("---")
    
    # Promedio si aplica
    if mostrar_promedio:
        promedio = total / contador
        
        partes = f"{promedio:.2f}".split(".")
        entero = partes[0]
        decimales = partes[1]
        
        entero_separado = ""
        for i, digito in enumerate(reversed(entero)):
            if i > 0 and i % 3 == 0:
                entero_separado = "." + entero_separado
            entero_separado = digito + entero_separado
        
        promedio_formateado = f"{entero_separado},{decimales}"
        
        nombre_alineado = "Promedio".ljust(ancho_nombre + (5 if mostrar_ranking else 0))
        lineas.append(f"{nombre_alineado} {moneda}{promedio_formateado}")
    
    return "\n".join(lineas)


# --- Pruebas (NO modificar) ---
if __name__ == "__main__":
    print("\n=== Ejercicio 2.3 ===")
    ventas = [
        ("Sala IMAX", 29250.0),
        ("Sala 3D", 15800.0),
        ("Sala Kids", 8900.0),
        ("Sala Premium", 21500.0),
    ]

    # Reporte simple
    print(construir_reporte("VENTAS DEL DÍA", ventas))

    # Reporte con ranking, sin promedio, en dólares
    print(construir_reporte("TOP SALAS", ventas, moneda="$",
                            mostrar_promedio=False, mostrar_ranking=True))

    # Salida esperada:
    # === Ejercicio 2.3 ===
    # ======= VENTAS DEL DÍA ========
    # Sala IMAX            Q29,250.00
    # Sala 3D              Q15,800.00
    # Sala Kids            Q8,900.00
    # Sala Premium         Q21,500.00
    # ---
    # Promedio             Q18,862.50
    #
    # ========= TOP SALAS ===========
    # #1 Sala IMAX            $29,250.00
    # #2 Sala 3D              $15,800.00
    # #3 Sala Kids            $8,900.00
    # #4 Sala Premium         $21,500.00
