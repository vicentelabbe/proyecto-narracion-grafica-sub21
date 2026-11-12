Ficha técnica — Visualización 01

El mito del abismo: trayectorias de futbolistas juveniles

Responsable de la visualización: Vicente Labbé

Archivo: cohorte_2019.csv

Formato: CSV

Registros: 25 futbolistas.

Variables: 18 columnas.

Cobertura: temporada 2019 y registros de las temporadas correspondientes a las edades de 22 y 24 años de cada futbolista (años 2019 a 2024).

Fuente consignada en la base: enlaces individuales a perfiles de Transfermarkt. Pendiente de verificar la correspondencia entre las cifras utilizadas y sus fuentes originales.

Objetivo de la base de datos

Registrar y comparar las trayectorias de una selección de 25 futbolistas vinculados al fútbol chileno en 2019.

La información permite examinar los minutos de participación inicial y su evolución en las temporadas correspondientes a las edades de 22 y 24 años.

Diccionario de variables

Variable	Descripción
id_jugador	Identificador único del futbolista
nombre_jugador	Nombre del jugador
fecha_nacimiento	Fecha de nacimiento
club_2019	Club registrado para 2019
posicion_especifica	Posición de juego
minutos_liga_2019	Minutos de liga registrados en 2019
año_edad_22	Año en que cumplió 22 años
club_edad_22	Club registrado para esa edad
division_edad_22	División o liga correspondiente
minutos_liga_edad_22	Minutos registrados a los 22 años
año_edad_24	Año en que cumplió 24 años
club_edad_24	Club registrado para esa edad
division_edad_24	División o liga correspondiente
minutos_liga_edad_24	Minutos registrados a los 24 años
ratio_retencion_22	Minutos a los 22 años divididos por los minutos de 2019, multiplicados por 100
estatus_carrera_24	Clasificación editorial de trayectoria profesional
notas_editoriales	Observaciones sobre la trayectoria del jugador
url_fuente_transfermarkt	Enlace al perfil individual de referencia

Categorías de trayectoria

La variable estatus_carrera_24 clasifica a los jugadores en tres grupos:

* Consolidado Primera División: 13 jugadores.
* Transferido al Extranjero: 8 jugadores.
* Ascenso / Segunda: 4 jugadores.

Estas cantidades corresponden a las etiquetas incluidas en el CSV y no constituyen una verificación independiente de la situación profesional de los futbolistas.

Procesamiento y calidad de datos

El archivo contiene 25 identificadores únicos, sin nombres duplicados ni celdas vacías.

Se comprobó que los valores de ratio_retencion_22 corresponden, con redondeo, a la relación entre los minutos registrados a los 22 años y los de 2019.

Observaciones metodológicas

* La base contiene futbolistas nacidos entre 1997 y 2000. Debe explicarse el criterio de inclusión de los jugadores de mayor edad dentro de la cohorte.
* No se documenta todavía el procedimiento original de selección de los 25 futbolistas.
* Las cifras individuales deben contrastarse con las fuentes indicadas.
* La clasificación de trayectoria requiere revisión: por ejemplo, Gabriel Suazo aparece clasificado como transferido al extranjero, aunque el registro correspondiente a sus 24 años señala a Colo-Colo.
* El ratio de minutos mide una comparación entre temporadas, pero no demuestra por sí mismo consolidación profesional.
* La muestra no debe presentarse como representativa de todos los futbolistas juveniles chilenos sin justificar su selección.

Relación con la webstory

La visualización 01 permite estudiar las trayectorias individuales y complementar la visualización 02, dedicada a comparar los minutos juveniles por club.

En conjunto, ambas buscan explorar la relación entre las oportunidades iniciales de participación y el desarrollo posterior de una carrera profesional.

Estado: ficha técnica preparada a partir del CSV original. Pendiente de verificación periodística y revisión por el equipo.
