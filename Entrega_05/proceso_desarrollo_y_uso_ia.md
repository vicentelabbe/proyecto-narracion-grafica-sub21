# Desarrollo y uso de IA

- Entregas anteriores: identidad gráfica reutilizada desde CSS; las visualizaciones se sustituyen por versiones exploratorias con datos ampliados.
- IA: asistencia código HTML/JS/Python.
- Bloqueos: Tribuna 403; API brasileña 404/400 para años antiguos; listado público limitado a 100.
- Pruebas pendientes: abrir en Safari y escritorio, selectores de gráficos, navegación, publicación GitHub Pages. 
- Pendiente: validar reglas anuales, identidades, posibles duplicados por club y trayectorias externas.


## Reconstrucción FBref, 25 de noviembre de 2026
El equipo aportó las tablas completas en el chat: 472 filas de 2015–2016, 447 de 2016–2017 y 382 de Transición 2017. La IA transcribió 331 filas relevantes (incluyendo candidatos mayores según edad reportada y tres casos sin nacimiento), no la totalidad de 1.301 filas. La extracción se revisó mediante claves de fila, minutos no negativos, titularidades <= partidos y minutos <= 90 × partidos. La transcripción debe ser cotejada por el equipo con el original. Se seleccionaron 259 registros de nacionalidad CHI según FBref y edad calculada al cierre del último año <=21: 86, 86, 87. Se excluyeron del cálculo principal los tres casos sin año de nacimiento; se preservan en un CSV aparte. La nacionalidad indicada por FBref puede diferir de ciudadanía/elegibilidad real. No se certifica cumplimiento de la norma ni cobertura real del universo. Se preservan cambios de club como filas distintas; recuento por temporada por nombre y nacimiento para FBref y playerId para la API. Se identificaron 163 combinaciones históricas de nombre y nacimiento, 108 con candidato único en la API, 1 ambiguo, 54 sin coincidencia automática; no son identidades confirmadas ni evidencia de abandono. Las temporadas 2015–2016 y 2016–2017 duran 30 fechas nominales y Transición 2017 15. El porcentaje de minutos programados es descriptivo y no equivale a minutos reglamentarios. Los resultados de 2018–2024 se preservan, incluso los minutos faltantes. La nueva base tiene 1.664 filas; la versión anterior se conserva en el ZIP original. No se ejecutó el notebook original del equipo ni se publicó GitHub Pages. 

Visualización histórica: gráfico de cobertura con y sin minutos, filtro de temporada, búsqueda y orden por minutos. Los otros dos gráficos no han sido recalculados con identidades históricas no validadas.

## Revisión posterior a Colab
Sofía ejecutó el notebook complementario y aportó Datos_reconstruidos_2015_2024.zip. Se compararon byte a byte sus ocho CSV con los incluidos en el paquete previo; coinciden. IA detectó cinco edades negativas y creó una capa analítica separada. Se verificaron ausencia de duplicados exactos y de minutos negativos o mayores a 90 × partidos cuando ambos datos existen. No se certificó la veracidad de la totalidad de la fuente. El equipo debe cotejar transcripción, revisar cruces y confirmar su autoría. 

Especificación: lectura de cinco capítulos, tres gráficos interactivos, búsqueda/orden/filtro histórico y menú de navegación; no requiere servidor de datos. La hipótesis pasa de una presunta caída universal a una pregunta abierta sobre trayectorias. 

## Rediseño y consolidación
El grupo solicitó fondo negro, verde fosforescente, tipografía deportiva y mayor espaciado. Se retiraron cifras ilustrativas no sustentadas de la portada y se corrigió el período a diez temporadas. La página mantiene los CSV analíticos y los filtros. El equipo debe confirmar autoría y revisar el relato.
