# Entrega 03 · Visualización individual 02 — Sofía Carvajal

**Proyecto grupal:** *El mito del abismo: las trayectorias del fútbol juvenil chileno*.
**Pieza individual:** *La barrera del trámite: ¿cuánto espacio dieron los clubes a sus jóvenes en 2019?*

## 1. Proceso de diseño y decisiones visuales

- **Gráfico:** barras horizontales por los 16 clubes de Primera División incluidos en la base de trabajo, ordenados alfabéticamente en la imagen exportada. Este formato facilita comparar magnitudes.
- **Eje X:** `minutos_sub21`, una suma por club de minutos juveniles registrados en el conjunto de datos.
- **Eje Y:** `club`.
- **Color:** `posicion_predominante` con una paleta diferenciada (volante `#0072B2`, lateral `#E69F00`, delantero `#009E73`). El color describe la clasificación del CSV; no equivale al desglose completo por posiciones.
- **Referencia:** línea discontinua de 1.350 minutos, exigencia mencionada para la temporada 2019. **No demuestra cumplimiento oficial** sin validar la equivalencia de las métricas.
- **Interacción:** en `visualizacion/vis_02.html` se despliegan detalles sobre jugadores utilizados y minutos por líneas de juego al situar el cursor sobre una barra.

## 2. Base utilizada y procesamiento

- **Archivo:** `minutos_sub21_clubes_2019.csv`, con 16 registros y nueve columnas.
- **Cobertura declarada:** clubes de Primera División de Chile, 2019.
- **Comprobación interna:** las cuatro columnas de minutos por posiciones suman el total de cada club; no se observaron vacíos en las variables usadas.
- **Valores destacados de esta base:** Colo-Colo, 3.640; O'Higgins, 3.370; Huachipato, 3.150; Deportes Iquique, 1.360. Diferencia máximo–mínimo: 2.280 minutos.
- **Distribución:** 8 clubes con volante como posición predominante; 4 con lateral; 4 con delantero. El total de defensas más volantes equivale al 70.5 % de los minutos agregados.

**Precaución metodológica:** la base provista para esta visualización no incluye trazabilidad a registros individuales ni fuentes primarias de cada valor. Es una base de trabajo en proceso de verificación. El total de minutos acumulados por varios futbolistas no es necesariamente la misma medida que los minutos ANFP computables para cumplir la cuota. Por tanto, el gráfico no acredita cumplimiento oficial ni permite deducir motivaciones tácticas. Los registros publicados por el Colegio de Entrenadores con cifras de la ANFP para 2019 difieren de varias filas del CSV.

Las coberturas históricas de la norma suelen denominarla regla Sub-20, aunque la webstory la aborda dentro del proyecto Sub-21. Deben revisarse las condiciones exactas de elegibilidad antes de publicar los datos como definitivos.

## 3. Preguntas que responde la visualización

1. ¿Cuáles son los clubes con mayor y menor cantidad de minutos en esta base y cuál es la distancia entre ellos?
2. ¿Qué posiciones aparecen como predominantes según la clasificación de los 16 clubes?
3. ¿Qué nuevas fuentes se requieren para evaluar cumplimiento normativo y compromiso formativo de manera rigurosa?

## 4. Archivos entregados

- `Ficha_Tecnica.md`: diccionario de variables y limitaciones.
- `minutos_sub21_clubes_2019.csv`: base de trabajo (sin modificar las cifras originales).
- `visualizacion/vis_02.html`: gráfico interactivo, exportado en Altair/Vega-Lite.
- `visualizacion/vis_02.jpg`: representación estática de la visualización.
- `visualizacion/cronica.md`: crónica individual (3051 caracteres, espacios incluidos).
- `scripts/codigo_para_visualizar_2.ipynb`: cuaderno de Python/Colab provisto para generar la visualización.

## 5. Fuentes y contrastes pendientes

- [Colegio de Entrenadores: tabla de minutos 2019 basada en registros ANFP](https://www.ctfutbol.cl/tabla-de-minutos-sub-20-primera-division/).
- [Pauta: explicativo de la regla juvenil en 2019](https://www.pauta.cl/deportes/2019/08/03/los-jugadores-sub-21-en-primera-division-del-futbol-chileno-2019.html).

**Estado de la evidencia:** la cifra de referencia normativa está respaldada por la prensa de la época, pero los valores de `minutos_sub21_clubes_2019.csv` requieren cotejo club por club con fuentes primarias antes de ser utilizados como registros oficiales.
