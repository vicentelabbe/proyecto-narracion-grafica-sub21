```python
# ==============================================================================
# Script de Carga y Exploración: Continuidad de Carrera Post-Regla Sub-21
# Pontificia Universidad Católica de Chile - Narración Gráfica (COM-208)
# Integrante: Sofía Carvajal
# ==============================================================================

import pandas as pd
import numpy as np

# 1. Cargar el dataset limpio
url = "https://raw.githubusercontent.com/vicentelabbe/proyecto-narracion-grafica-sub21/main/Entrega_02/Carvajal_Sofia_seguimiento_carrera/continuidad_carrera_post21_limpio.csv"

try:
    df = pd.read_csv(url)
except Exception:
    df = pd.read_csv("continuidad_carrera_post21_limpio.csv")

# 2. Vista preliminar de los datos
print("--- PRIMERAS 5 FILAS DEL DATASET DE CONTINUIDAD ---")
print(df.head())

# 3. Estructura y tipos de datos
print("\n--- INFORMACIÓN GENERAL DEL DATAFRAME ---")
df.info()

# 4. Tabla Dinámica 1: Distribución del estatus de consolidación a los 24 años
pivot_estatus = pd.pivot_table(
    df,
    values=['id_jugador', 'minutos_edad_24'],
    index=['estatus_consolidacion'],
    aggfunc={'id_jugador': 'count', 'minutos_edad_24': 'mean'}
).round(1).rename(columns={'id_jugador': 'total_jugadores', 'minutos_edad_24': 'promedio_minutos_24'})

print("\n--- TABLA DINÁMICA 1: DESTINO Y MINUTOS A LOS 24 AÑOS ---")
print(pivot_estatus)

# 5. Tabla Dinámica 2: Retención de minutos a los 22 años según división
pivot_division = pd.pivot_table(
    df,
    values=['ratio_retencion_minutos_22', 'minutos_edad_22'],
    index=['division_edad_22'],
    aggfunc={'ratio_retencion_minutos_22': 'mean', 'minutos_edad_22': 'mean'}
).round(1)

print("\n--- TABLA DINÁMICA 2: RETENCIÓN DE MINUTOS SEGÚN DIVISIÓN A LOS 22 AÑOS ---")
print(pivot_division)

```
