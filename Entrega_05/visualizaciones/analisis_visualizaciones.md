# Visualizaciones — beta

| Elemento | Mensaje | Interacción | CSV |
|---|---|---|---|
| Cobertura | Distinguir registros observados y faltantes por temporada | Tooltip | cobertura_beta.csv |
| Explorador histórico | Consultar minutos y clubes de jugadores 2015–2017 | Temporada, búsqueda y orden | juveniles_fbref_2015_2017.csv |
| Clubes (evolución de vis_02) | Comparar espacio registrado dentro de cada torneo | Selector de temporada y tooltip | clubes_beta.csv |
| Edades (evolución de vis_01) | Contrastar continuidad de minutos entre 21 y 24 | Promedio o mediana | edades_beta.csv; comparacion_edades_completa.csv |

La visualización de clubes extiende el enfoque original de 2019 sin presentar la cuota reglamentaria como línea de referencia. El resultado de edad contradice la expectativa de caída general dentro de los 46 casos completos, pero la selección puede excluir trayectorias discontinuas. Los minutos absolutos no son equivalentes entre temporadas de distinta duración. La tabla histórica muestra una normalización nominal para 30 o 15 fechas; no mide cumplimiento. Los asteriscos en clubes advierten valores faltantes; un club sin ningún minuto observado no se representa como cero. Se conservan las filas por club y los posibles cambios de equipo; no se ha verificado si existen totales acumulados de API.

Código: `codigo/generar_beta.py` (pandas), `codigo/script.js` (Plotly.js y JavaScript), HTML/CSS y `data.js`. Referencias visuales en `imagenes/` obtenidas de la página con Chromium. Versiones anteriores conservadas en código y respaldo. No se incorporan cruces históricos no confirmados a la comparación longitudinal.
