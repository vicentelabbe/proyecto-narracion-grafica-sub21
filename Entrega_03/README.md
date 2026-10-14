# Documentación Metodológica y Proceso de Visualización - Integrante 01

## 1. Proceso de Diseño Visual en Altair y Decisiones Tomadas

Para comunicar la evolución de la cohorte 2019 a través del tiempo, se seleccionó un diagrama de dispersión multivariable interactivo (*scatter plot*) desarrollado en Altair, privilegiando la precisión geométrica por sobre el adorno visual:

* **Posición en los ejes (X e Y):**  
  * Eje X (`minutos_liga_2019`): Representa el punto de partida bajo la regla reglamentaria.  
  * Eje Y (`minutos_liga_edad_24`): Mide la consolidación competitiva cinco años después.  
  * **Línea diagonal de referencia ($x=y$):** Se integró una recta punteada neutra. Todo punto situado por encima de la diagonal identifica a un futbolista que disputó más minutos a los 24 años que en su temporada Sub-21, aislando visualmente el crecimiento de la involución.
* **Canal de Color:** Se asignó a la variable nominal `estatus_carrera_24` utilizando la paleta accesible Okabe-Ito (`#0072B2`, `#009E73`, `#D55E00`), garantizando legibilidad ante daltonismo y diferenciando con claridad el destino divisional.
* **Canal de Tamaño:** El área de cada punto codifica los `minutos_liga_edad_22`, permitiendo observar en una sola marca si la transición intermedia fue de titularidad o de ostracismo.
* **Canal de Forma:** Se distinguen círculos para los nacidos a partir de 1999 y rombos para los nacidos antes de 1999, transparentando las excepciones reglamentarias identificadas en la auditoría.
* **Interactividad y Scrollytelling:** Se programó un filtro dinámico vinculado a la leyenda (`selection_point`), de modo que al hacer clic en una categoría (ej. *Transferido al Extranjero*) los demás puntos se atenúan a un 15% de opacidad, facilitando el análisis aislado para la webstory.

## 2. Base de Datos Utilizada y Procesamiento

* **Fuente seleccionada:** `cohorte_2019.csv` (25 registros).  
* **Criterio de selección:** Es una generación completamente cerrada en el plano temporal (nacidos entre 1997 y 2000), cuyos 22 y 24 años biológicos ya concluyeron en la vida real entre 2019 y 2024, eliminando cualquier margen de proyección o dato especulativo.
* **Transformaciones previas en Python:** Se recalculó y validó la consistencia del ratio de retención porcentual a los 22 años, se extrajo el año de nacimiento desde la fecha biográfica y se categorizó el criterio reglamentario estricto.

## 3. Preguntas que Responde la Visualización

1. **¿Existe correlación directa entre sumar muchos minutos Sub-21 y consolidarse a los 24 años?**  
   *La visualización muestra que no necesariamente: jugadores con menos de 700 minutos en 2019 (ej. Williams Alarcón o Carlos Palacios) alcanzaron mayor continuidad y cotización que futbolistas que superaron los 1.500 minutos en su temporada de debut.*
2. **¿Qué patrón define a los jugadores exportados al extranjero?**  
   *Al aislar los puntos verdes, se evidencia que la salida internacional se concentra en futbolistas que tuvieron picos de rendimiento sobresalientes a los 22 años (tamaño de punto elevado).*
3. **¿A quiénes afecta verdaderamente el estancamiento deportivo?**  
   *El cuadrante inferior derecho expone a los canteranos que tuvieron alto minutaje reglamentario pero que a los 24 años cayeron por debajo de los 1.000 minutos o descendieron a categorías de ascenso.*
