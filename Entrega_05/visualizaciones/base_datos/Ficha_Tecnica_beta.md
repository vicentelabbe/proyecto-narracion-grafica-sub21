# Fichas técnicas de las bases de la beta

## Fuentes y extracción
- FBref: [2015–2016](https://fbref.com/en/comps/35/2015-2016/stats/2015-2016-Liga-de-Primera-Stats), [2016–2017](https://fbref.com/en/comps/35/2016-2017/stats/2016-2017-Liga-de-Primera-Stats), [Transición 2017](https://fbref.com/en/comps/35/2017/stats/2017-Liga-de-Primera-Stats). Tablas copiadas por Sofía el 25/11/2026; 331 filas relevantes transcritas con IA, 259 seleccionadas por nacimiento, nacionalidad reportada CHI y edad al cierre <=21. Tres nacimientos desconocidos preservados aparte. No se conserva aquí la totalidad de las tablas originales.
- Classificação Geral: [API 2018](https://api.classificacaogeral.com.br/v1/competitions/265/editions/2018/players), sustituir año 2018 por cada año hasta 2024. Extracción paginada y respaldos previos del equipo. Notebook facilitado por la profesora y archivo de fuentes incluidos. No se verificó disponibilidad en vivo en esta revisión.

## Archivos utilizados
| CSV | Unidad | Campos principales | Tratamiento |
|---|---|---|---|
| base_integrada_2015_2024.csv | Registro jugador-club-temporada | nombre, playerId, club, temporada, nacimiento, edad, minutos, origen | Salida de Colab sin modificar |
| base_analitica_beta.csv | Misma unidad | mismos campos | Excluye edades negativas; 1.659 filas |
| exclusiones_edad.csv | Registro excluido | mismos campos | Cinco edades negativas, todos sin minutos |
| cobertura_beta.csv | Temporada | registros, con_minutos, sin_minutos, minutos | Conteos y suma de observados |
| clubes_beta.csv | Club-temporada | club, temporada, registros, con_minutos, sin_minutos, minutos | Suma de observados; nulo si no hay ninguno |
| juveniles_fbref_2015_2017.csv | Jugador-club-torneo | fila original, nombre, nacimiento, minutos, porcentaje nominal, fuente | 259 filas; porcentaje = minutos / (90 × fechas nominales) ×100 |
| comparacion_edades_completa.csv | Jugador ID | minutos_21 a minutos_24 | 46 casos completos de API; conserva ceros explícitos |
| edades_beta.csv | Edad | promedio, mediana, n | Agregación de 46 casos |

Todos los CSV en UTF-8, separados por coma. Minutos son numéricos; vacío significa desconocido, no cero. Edad al cierre es año de cierre menos año de nacimiento. La selección cronológica no certifica nacionalidad legal ni elegibilidad reglamentaria. La comparación por edad mantiene el análisis anterior, sin verificar acumulaciones entre clubes ni normalizar duración. Los 108 cruces únicos y 1 ambiguo de 163 combinaciones históricas requieren identificación externa; 54 no coincidieron automáticamente. No concluir abandono por falta de coincidencia.

## Replicación
Ejecutar notebook complementario con ZIP original para obtener la base integrada; luego desde el repositorio `python Entrega_05/visualizaciones/codigo/generar_beta.py` (pandas). Genera CSV analíticos y `docs/data.js`. Las visualizaciones funcionan con Plotly.js local. Fuente adicional de contraste reglamentario indicada en Entrega 04: [Pauta 2019](https://www.pauta.cl/deportes/2019/08/03/los-jugadores-sub-21-en-primera-division-del-futbol-chileno-2019.html); verificar bases oficiales año a año antes de afirmar cumplimiento.
