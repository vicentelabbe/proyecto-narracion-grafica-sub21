# ==============================================================================
# Script de Carga y Exploración de Datos: Minutaje Sub-21
# Pontificia Universidad Católica de Chile - Narración Gráfica (COM-208)
# Integrante: Vicente Labbé Reyes
# ==============================================================================

import pandas as pd
import numpy as np

# 1. Cargar el dataset limpio
url = "https://raw.githubusercontent.com/vicentelabbe/proyecto-narracion-grafica-sub21/main/Entrega_02/Labbe_Vicente_minutos_sub21/minutaje_sub21_chile_limpio.csv"

try:
    df = pd.read_csv(url)
except Exception:
    df = pd.read_csv("minutaje_sub21_chile_limpio.csv")

# 2. Visualización de las primeras filas del DataFrame
print("--- PRIMERAS 5 FILAS DEL DATAFRAME ---")
print(df.head())

# 3. Resumen estructural y tipos de datos
print("\n--- INFORMACIÓN DE TIPOS Y VALORES NULOS ---")
df.info()

# 4. Tabla dinámica 1: Minuto promedio de salida por posición táctica
pivot_posicion = pd.pivot_table(
    df[df['partidos_sustituido'] > 0],
    values=['minuto_promedio_salida', 'minutos_sub21_regla'],
    index=['posicion_agrupada'],
    aggfunc={'minuto_promedio_salida': 'mean', 'minutos_sub21_regla': 'sum'}
).round(1)

print("\n--- TABLA DINÁMICA 1: SUSTITUCIÓN Y MINUTOS POR POSICIÓN ---")
print(pivot_posicion)

# 5. Tabla dinámica 2: Participación total por Club
pivot_club = pd.pivot_table(
    df,
    values=['partidos_titular', 'minutos_totales_liga'],
    index=['club'],
    aggfunc={'partidos_titular': 'mean', 'minutos_totales_liga': 'sum'}
).round(1)

print("\n--- TABLA DINÁMICA 2: TITULARIDADES Y MINUTOS POR CLUB ---")
print(pivot_club)
