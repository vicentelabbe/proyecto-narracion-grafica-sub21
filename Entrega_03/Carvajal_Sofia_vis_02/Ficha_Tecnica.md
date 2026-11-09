# Ficha técnica · Visualización 02 (2019)

| Campo | Detalle |
|---|---|
| Archivo | `minutos_sub21_clubes_2019.csv` |
| Cobertura de la base | 16 clubes de Primera División de Chile, temporada atribuida: 2019 |
| Unidad de análisis | Club |
| Fuente inmediata | CSV entregado al equipo (procedencia primaria no documentada) |
| Estado | Base de trabajo, cifras pendientes de contraste |

## Diccionario de variables

| Variable | Tipo | Uso en la visualización | Descripción |
|---|---|---|---|
| `club` | Texto nominal | Eje Y | Club de Primera División |
| `minutos_sub21` | Entero | Eje X | Total consignado de minutos juveniles del club |
| `jugadores_sub21` | Entero | Tooltip | Número consignado de jugadores utilizados |
| `posicion_predominante` | Texto nominal | Color | Grupo posicional más utilizado, según clasificación original |
| `min_defensas` | Entero | Tooltip | Minutos agrupados en defensas, incluidos laterales |
| `min_volantes` | Entero | Tooltip | Minutos de mediocampistas |
| `min_delanteros` | Entero | Tooltip | Minutos de atacantes |
| `min_arqueros` | Entero | Dato de respaldo | Minutos de porteros |
| `cumplio_regla` | Texto categórico (`Si`) | No graficado | Clasificación incluida por quien construyó el CSV; **no validada** con registros de cumplimiento ANFP |

## Comprobaciones y advertencias

1. Hay 16 registros sin valores faltantes en las columnas utilizadas y, para cada fila, `min_defensas + min_volantes + min_delanteros + min_arqueros = minutos_sub21`.
2. El total agregado del archivo es 33.495 minutos; corresponde a la suma de los valores contenidos en **esta base**, no a una cifra oficial verificada.
3. El umbral de 1.350 minutos está respaldado para 2019, pero debe revisarse si el campo de total juvenil incluye simultaneidad de jugadores y qué metodología aplica para el cómputo ANFP.
4. Registros de seguimiento publicados en 2019 por el Colegio de Entrenadores a partir de la ANFP muestran cifras diferentes de varias filas; no se declara cumplimiento generalizado.
5. `posicion_predominante` mezcla categorías tácticas específicas (lateral) con grupos más amplios (volante y delantero). Se mantiene la clasificación original sin reinterpretación.

## Fuentes para la auditoría

- [Tabla 2019, Colegio de Entrenadores — registros ANFP](https://www.ctfutbol.cl/tabla-de-minutos-sub-20-primera-division/).
- [Contexto 2019, Pauta](https://www.pauta.cl/deportes/2019/08/03/los-jugadores-sub-21-en-primera-division-del-futbol-chileno-2019.html).
