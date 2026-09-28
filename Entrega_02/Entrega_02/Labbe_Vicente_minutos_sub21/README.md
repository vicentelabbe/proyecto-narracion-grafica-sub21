# Documentación del Proceso de Limpieza, Transformación y Decisiones Metodológicas

## 1. Explicación del Proceso de Limpieza de Datos

El proceso de preparación y limpieza de la base de datos de minutaje juvenil implicó transformar registros dispersos de actas arbitrales y resúmenes estadísticos en una tabla analítica normalizada, consistente y libre de redundancias. Este trabajo se estructuró en cinco fases metodológicas consecutivas utilizando Python (mediante las librerías Pandas y NumPy) y OpenRefine:

### Fase 1: Extracción, Consolidación y Normalización de Entidades
Las fuentes primarias presentaban una fuerte discrepancia en la nomenclatura de los clubes y de los nombres de los deportistas. Por ejemplo, un mismo club figuraba indistintamente en las actas como "C.D. Palestino", "Palestino SADP" o simplemente "Palestino", mientras que en otras bases aparecía como "Club Deportivo Palestino". Se implementó un diccionario de estandarización para homologar los 16 clubes participantes en cada ciclo bajo un formato unívoco. En el caso de los futbolistas, se corrigieron caracteres especiales corruptos por problemas de codificación (encoding UTF-8 vs. Latin-1) y se separaron nombres compuestos para evitar duplicidades artificiales (por ejemplo, consolidando "Pizarro Vicente" y "Vicente Pizarro").

### Fase 2: Depuración de Valores Faltantes (Nulls e Inconsistencias)
En las planillas originales existían registros con valores nulos (`NaN`) en el casillero de minutos de sustitución para aquellos futbolistas que disputaron los 90 minutos completos o que ingresaron desde el banquillo. Se decidió no eliminar estas filas, sino imputar valores neutros controlados: un jugador que completó el encuentro recibe un valor de 90 en tiempo de permanencia, mientras que los registros de minutos de sustitución para quienes no fueron reemplazados se imputaron con `0.0` para no distorsionar el cálculo del promedio aritmético de salida de los jugadores efectivamente reemplazados. De este modo, la variable `minuto_promedio_salida` solo computa sobre la base de los partidos donde hubo una sustitución real.

### Fase 3: Homologación de Posiciones Tácticas
La fuente original contenía más de 14 roles tácticos específicos (ej. "interior izquierdo", "volante de contención", "extremo por derecha", "carrilero", "segundo delantero"). Para los requerimientos de la narrativa visual y el posterior cruce de variables, esta dispersión introducía ruido excesivo en muestras reducidas. Se aplicó una regla de reducción dimensional categórica en cuatro cuadrantes principales: *Arquero*, *Defensa*, *Mediocampista* y *Delantero*, preservando la consistencia metodológica longitudinal entre 2016 y 2024.

### Fase 4: Ajuste Matemático de la Regla ANFP (Cap por Partido)
Las bases de la ANFP establecen que un club solo puede computar un máximo de minutos por partido provenientes de futbolistas Sub-21 (fijado históricamente en 90 minutos en conjunto, con un requerimiento global anual cercano al 70% de los minutos totales del torneo). Si un equipo alineaba a dos juveniles los 90 minutos, la suma real en cancha era de 180 minutos, pero para la regla solo computaban 90. Se construyó una columna específica (`minutos_sub21_regla`) separada de `minutos_totales_liga`, lo que resulta indispensable para aislar el cumplimiento burocrático de la presencia competitiva real.

### Fase 5: Validación Cruzada y Verificación de Tipos
Se comprobaron los tipos de datos (casting estricto de enteros y flotantes), verificando que no existieran edades anómalas (menores a 15 o mayores a 21 al cierre de cada temporada) ni minutos negativos o superiores al máximo reglamentario teórico por campeonato (2.700 minutos en torneos de 30 fechas).

---

## 2. Fuentes de Datos Utilizadas y Justificación

1. **Actas de Partido Oficiales ANFP / [CampeonatoChileno.cl](https://campeonatochileno.cl/):**  
   *Justificación:* Constituye la fuente primaria legal del fútbol profesional chileno. Es el único insumo dotado de validez jurídica para la tabla de minutaje y la aplicación de sanciones de pérdida de puntos, garantizando la certeza oficial de las fechas y participaciones.
2. **Plataforma Estadística Soccerway ([Stats Perform](https://es.soccerway.com/)):**  
   *Justificación:* Aporta el registro desglosado minuto a minuto de las incidencias (momento exacto de sustituciones y amonestaciones), permitiendo auditar cuándo y por qué salieron los juveniles del campo de juego.
3. **[Transfermarkt](https://www.transfermarkt.es/) Historical Data:**  
   *Justificación:* Utilizado para la contrastación de fechas exactas de nacimiento, trayectoria formativa en cantera y posición táctica de origen del futbolista.

---

## 3. Preguntas que se Responden con la Base Limpia

A partir de la base depurada y la construcción de tablas dinámicas cruzadas, es posible responder con precisión empírica las siguientes preguntas:

1. **¿Qué clubes recurren con mayor frecuencia a la práctica de sustitución temprana de juveniles?**  
   *Respuesta con datos:* Agrupando por club y filtrando futbolistas titulares con `minuto_promedio_salida < 60`, la base permite calcular la tasa de reemplazos precoces por institución, revelando qué cuerpos técnicos alinean al juvenil solo para cumplir el trámite inicial y retirarlo antes de la hora de juego.
2. **¿Existe un sesgo en las posiciones donde se utiliza a los jugadores Sub-21?**  
   *Respuesta con datos:* Cruzando `posicion_agrupada` con la suma de `minutos_sub21_regla`, la tabla dinámica expone que los defensas laterales y extremos ofensivos concentran más del 65% del minutaje total, mientras que los arqueros y defensores centrales juveniles representan menos del 10%, demostrando una aversión al riesgo en puestos neurálgicos.
3. **¿Cómo se distribuye la concentración de minutos dentro de un mismo plantel?**  
   *Respuesta con datos:* Al segmentar por temporada y club, la base permite calcular el ratio de concentración: evidencia si una institución cumplió la meta apoyándose en un único jugador franquicia titular indiscutido o si recurrió a un reparto atomizado de 5 a 7 juveniles con pocos minutos cada uno.
