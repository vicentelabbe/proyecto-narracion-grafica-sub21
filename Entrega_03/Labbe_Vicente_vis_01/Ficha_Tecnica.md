# Ficha técnica · vis_01

Fuente: `cohorte_2019.csv` (25 filas). Estado: provisional, en verificación (ver README).

| Variable | Tipo | Uso en vis_01 | Notas editoriales |
|---|---|---|---|
| id_jugador | texto | no se grafica | Correlativo CHI-2019-01 a 25 |
| nombre_jugador | texto | tooltip, etiquetas | Sin tildes en la base |
| fecha_nacimiento | fecha (AAAA-MM-DD) | deriva `anio_nac` y `regla` | 5 nacidos antes de 1999 |
| club_2019 | categórica | tooltip | Una fila trae dos clubes ("Colon / San Antonio") |
| posicion_especifica | categórica | tooltip | Valores fuera de la taxonomía del enunciado |
| minutos_liga_2019 | entero | eje X | Todos múltiplos de 10: verificar |
| año_edad_22 | entero | no se grafica | Validado: nacimiento + 22 |
| club_edad_22 | categórica | tooltip | Cambios de club a mitad de año: criterio por definir |
| minutos_liga_edad_22 | entero | tamaño | Todos múltiplos de 10: verificar |
| año_edad_24 | entero | no se grafica | Validado: nacimiento + 24 |
| club_edad_24 | categórica | tooltip | Una fila trae dos clubes ("San Lorenzo / Belgrano") |
| minutos_liga_edad_24 | entero | eje Y | Todos múltiplos de 10: verificar |
| ratio_retencion_22 | decimal | tooltip | Recalculado: 25 de 25 coinciden; 100,0 por construcción en 3 casos |
| estatus_carrera_24 | categórica (3 niveles) | color | 13 consolidado, 8 extranjero, 4 ascenso / segunda |
| notas_editoriales | texto | no se grafica | Afirmaciones biográficas sin fuente individual |
| url_fuente_transfermarkt | URL | no se grafica | IDs casi consecutivos en varios perfiles: abrir y confirmar |
| anio_nac | entero (derivada) | deriva `regla` | Año de `fecha_nacimiento` |
| regla | categórica (derivada) | forma | "Nacido en 1999 o después" / "antes de 1999 (revisar)" |
