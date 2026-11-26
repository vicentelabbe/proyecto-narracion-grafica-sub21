# El mito del abismo

**¿Qué ocurre con las oportunidades de los futbolistas jóvenes cuando superan los 21 años?**

Webstory beta · Narración Gráfica de No Ficción (COM-208) · Facultad de Comunicaciones, Pontificia Universidad Católica de Chile.

**Autores:** Sofía Carvajal y Vicente Labbé.

## Resumen del reportaje

Debutar en Primera División no es lo mismo que mantenerse en ella. A partir de la discusión sobre la regla juvenil del fútbol chileno, exploramos cómo se distribuyen los minutos de juego entre clubes y qué ocurre con la continuidad competitiva de los futbolistas al avanzar en edad. Ampliamos nuestro análisis inicial de 2019 e incorporamos registros de las temporadas comprendidas entre 2015 y 2024. Nuestra webstory combina gráficos interactivos, un explorador histórico y un análisis de las trayectorias observadas entre los 21 y los 24 años.

## Hipótesis: del supuesto abismo a una pregunta abierta

Nuestra hipótesis inicial planteaba que los futbolistas jóvenes pierden oportunidades de juego al superar la edad juvenil. El desafío es distinguir entre el acceso inicial a Primera División y la posibilidad de sostener una trayectoria competitiva.

Al ampliar nuestra investigación, observamos un resultado que matiza nuestra hipótesis: entre los 46 futbolistas con minutos registrados a los 21, 22, 23 y 24 años en la fuente de 2018–2024, el promedio aumentó de 1.068 a 1.318 minutos entre los extremos del período observado. De ellos, 29 aumentaron su minutaje y 17 lo redujeron.

Por lo tanto, los datos de esta muestra no respaldan una caída generalizada después de los 21 años. Sin embargo, no permiten descartar que exista una pérdida de oportunidades entre quienes dejaron de aparecer en los registros o tienen información incompleta. Tampoco permiten atribuir causalmente las variaciones a la regla juvenil. El hallazgo desplaza el foco desde una caída supuestamente universal hacia las diferencias entre trayectorias y las dificultades de observar la continuidad de todos los jugadores.

## Datos y alcance

La integración de datos reproducida en Colab contiene 1.664 registros. Se excluyeron cinco registros con edades negativas, dejando 1.659 filas analíticas: 1.406 con minutos disponibles y 253 sin ese dato. Los 259 registros históricos de 2015–2017 provienen de la extracción juvenil de 1.301 filas aportadas por el equipo. Son registros, no necesariamente personas distintas. La edad cronológica al cierre del año no equivale a la elegibilidad reglamentaria. Los cruces nominales históricos requieren corroboración y los minutos absolutos deben interpretarse considerando la duración de los torneos.

## Autoría

| Elemento | Sofía Carvajal | Vicente Labbé |
|---|---|---|
| Definición del tema y formulación de la hipótesis | Participación | Participación |
| Investigación y búsqueda de datos durante el semestre | — | Responsable principal |
| Recopilación complementaria de tablas históricas 2015–2017 | Responsable | — |
| Visualización original de minutos juveniles por club (2019) | Autora | — |
| Visualización original de trayectorias de la cohorte 2019 | — | Autor |
| Wireframes, prototipo, perfiles de persona y mapa de viaje | Responsable | — |
| Identidad visual original | Responsable | — |
| Redacción de textos periodísticos | Participación | Participación |
| Desarrollo e integración de la webstory beta | Participación | Participación |
| Ejecución del notebook de reconstrucción en Colab | Ejecución | — |
| Revisión y decisiones del rediseño de la beta | Participación | Participación |

Distribuimos las responsabilidades individuales y trabajamos en conjunto en la definición del tema, la hipótesis, la redacción y la integración de la webstory. Utilizamos ChatGPT como herramienta de apoyo para la transcripción e integración de datos, la programación, la exploración de resultados y las propuestas de redacción. El detalle de este apoyo se encuentra en el documento de proceso de desarrollo y uso de IA. Tenemos pendiente la validación editorial y técnica definitiva de la versión publicada.

## Estructura y fuentes

- [Webstory beta](../docs/index.html): HTML, CSS, JavaScript y Plotly.js.
- [Proceso de desarrollo y uso de IA](proceso_desarrollo_y_uso_ia.md).
- [Análisis de visualizaciones](visualizaciones/analisis_visualizaciones.md), código, imágenes, CSV y fichas técnicas.
- [Análisis de diseño](diseno-historia/analisis_diseno.md) y recursos originales de las entregas anteriores.
- [Pruebas técnicas](pruebas_tecnicas.md).

Fuentes principales: [FBref 2015–2016](https://fbref.com/en/comps/35/2015-2016/stats/2015-2016-Liga-de-Primera-Stats), [FBref 2016–2017](https://fbref.com/en/comps/35/2016-2017/stats/2016-2017-Liga-de-Primera-Stats), [FBref 2017](https://fbref.com/en/comps/35/2017/stats/2017-Liga-de-Primera-Stats) y [API Classificação Geral (ejemplo de temporada 2018)](https://api.classificacaogeral.com.br/v1/competitions/265/editions/2018/players).

Los archivos originales de 2019 se conservan como antecedentes y no deben confundirse con las visualizaciones vigentes de la beta. La comprobación de la publicación en GitHub Pages y la revisión final del contenido quedan pendientes de registro.
