
## Visualización 01 - Vicente Labbé

### Trayectorias de los futbolistas Sub-21

**Objetivo:** explorar las trayectorias posteriores de los futbolistas jóvenes analizados en el proyecto.

### Relación con la webstory

Esta visualización constituye una parte central de "El mito del abismo", porque permite trasladar el foco desde las oportunidades de participación juvenil hacia las trayectorias posteriores de los jugadores.

Mientras la visualización 02 compara el minutaje de los clubes, esta visualización se concentra en las trayectorias individuales de los futbolistas.

### Archivos de respaldo

- Base de datos: base_datos/cohorte_2019.csv
- Código Python: codigo/codigo_para_visualizar_1.ipynb
- Gráfico HTML: codigo/vis_01.html
- Imagen referencial: imagenes/vis_01.jpg

### Análisis periodístico pendiente de validación

### Resultados exploratorios de la cohorte

La base de trabajo contiene 25 futbolistas vinculados
a la temporada 2019.

Según la variable estatus_carrera_24, los jugadores
se distribuyen de la siguiente manera:

- 13 jugadores (52%): Consolidado Primera División.
- 8 jugadores (32%): Transferido al Extranjero.
- 4 jugadores (16%): Ascenso / Segunda.

Además, 17 de los 25 jugadores registran más minutos
en la temporada correspondiente a sus 24 años que
en la temporada 2019.

Estos resultados son descriptivos y preliminares.

### Limitaciones

Las categorías de trayectoria y los minutos deben
verificarse con las fuentes originales.

Las temporadas comparadas corresponden a distintas
edades y contextos competitivos.

La selección de 25 jugadores no permite generalizar
los resultados a todos los futbolistas juveniles
chilenos.

Estos registros no permiten demostrar por sí solos
una relación causal entre la regla Sub-21 y la
continuidad profesional.

### Estado

Visualización incorporada técnicamente a la webstory. Pendiente de revisión periodística y pruebas de funcionamiento.

## Visualización 02 - Sofía Carvajal

### Minutos Sub-21 por club en 2019

**Objetivo:** comparar los minutos juveniles registrados en los 16 clubes de Primera División chilena incluidos en la base de datos de 2019.

### Tipo de visualización

Se desarrolló un gráfico de barras horizontales mediante Python y Altair.

- Eje horizontal: minutos Sub-21 por club.
- Eje vertical: clubes de Primera División.
- Colores: posición predominante registrada en cada club.
- Línea de referencia: 1.350 minutos.
- Interactividad: información adicional al explorar las barras.

### Relación con la webstory

La visualización aporta una mirada institucional a la historia "El mito del abismo".

Mientras las otras secciones investigan las trayectorias individuales de los futbolistas, este gráfico permite comparar la participación juvenil entre instituciones.

Su función es mostrar las diferencias de minutaje registradas en la base y aportar contexto al análisis de las oportunidades que tuvieron los jugadores.

### Interpretación de los datos

En la base de trabajo, los 16 clubes presentan cifras diferentes de minutos juveniles.

El gráfico permite identificar cuáles registran los mayores y menores minutajes y compararlos con la referencia utilizada.

Sin embargo, estos registros requieren contrastación con fuentes oficiales antes de formular conclusiones definitivas sobre el cumplimiento reglamentario.

Los minutos disputados tampoco permiten determinar, por sí solos, las motivaciones deportivas de cada club.

### Archivos de respaldo

- Base de datos: base_datos/minutos_sub21_clubes_2019.csv
- Ficha técnica: base_datos/Ficha_Tecnica.md
- Visualización HTML: codigo/vis_02.html
- Código Python: notebook .ipynb en codigo/
- Imagen: imagenes/imagen_visualizacion.png

### Estado

Visualización desarrollada e incorporada técnicamente a la webstory.

Pendiente: verificación de las fuentes originales, revisión del contenido y pruebas de visualización en distintos dispositivos.
