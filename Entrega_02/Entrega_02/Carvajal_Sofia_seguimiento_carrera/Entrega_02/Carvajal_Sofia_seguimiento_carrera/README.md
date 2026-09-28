 Documentación del Proceso de Limpieza, Transformación y Decisiones Metodológicas

## 1. Explicación del Proceso de Limpieza de Datos

El objetivo central de este dataset consistió en construir una cohorte longitudinal para medir qué ocurre verdaderamente con los futbolistas chilenos una vez que cruzan la barrera de los 21 años y pierden la protección de la regla de minutaje. La información original se encontraba fragmentada en fichas individuales de jugadores en bases de datos biográficas y tablas de transferencias de diversos sitios web. Para consolidar una base depurada, replicable y transparente, se aplicó el siguiente procedimiento metodológico:

### Paso 1: Definición del Criterio de Cohorte y Filtrado Inicial
No todos los juveniles que jugaron minutos aislados podían considerarse parte de una cohorte representativa. Para evitar distorsiones causadas por jugadores que debutaron apenas un par de minutos en tiempo de adición, se fijó un umbral de entrada de al menos 450 minutos disputados (equivalente a 5 partidos completos) en una sola temporada de Primera División bajo estatus Sub-21. Esto redujo el universo a 180 futbolistas con rodaje significativo entre las temporadas 2016 y 2021.

### Paso 2: Normalización de Nombres y Emparejamiento de Identificadores
Debido a que los portales biográficos suelen registrar nombres completos con dos apellidos o invertir el orden de nombres y apellidos, se utilizó Python para estandarizar cadenas de texto (removiendo acentos mal procesados, eliminando espacios redundantes y generando un `id_jugador` homologado). Esto garantiza la interoperabilidad absoluta con la base de minutaje del Integrante 01.

### Paso 3: Resolución de Inconsistencias en Jugadores a Préstamo y Cambios de División
Uno de los mayores desafíos metodológicos fue el tratamiento de jugadores cedidos a divisiones menores durante el año en que cumplieron 22 años. En las bases sin limpiar, muchos de estos futbolistas figuraban como "activos" en su club de origen en Primera División, a pesar de haber jugado toda la temporada en Primera B o Segunda Profesional. Se contrastaron manualmente las planillas efectivas de juego para asignar la división real donde el jugador disputó sus minutos, evitando sobreestimar la permanencia en la máxima categoría.

### Paso 4: Tratamiento de Valores Faltantes (Inactividad, Lesiones o Retiro)
Aquellos jugadores que no registraron minutos a los 22 o 24 años por encontrarse sin club, haber sido relegados al equipo de proyección o sufrir lesiones de larga duración aparecían originalmente con valores nulos o celdas vacías. Se decidió imputar numéricamente `0` en la columna de minutos y categorizar la variable divisional como `Sin Club/Retirado`. Esto permitió que las funciones estadísticas y promedios no omitieran a los deportistas descartados por el sistema, lo cual hubiese introducido un sesgo de supervivencia grave en la investigación.

### Paso 5: Creación de Variables Analíticas Propias
Se generaron dos métricas derivadas clave: el `ratio_retencion_minutos_22` (que calcula matemáticamente la pérdida porcentual de protagonismo en cancha de un año a otro) y la variable categórica `estatus_consolidacion`, que agrupa el desenlace del jugador para alimentar directamente visualizaciones interactivas de flujo y supervivencia.

---

## 2. Fuentes de Datos Utilizadas y Justificación

1. **Transfermarkt Historical Career Records:**  
   *Justificación:* Permite acceder al historial cronológico detallado de fichajes, cesiones, divisiones y minutos disputados por temporada para cada jugador registrado profesionalmente.
2. **Base de Datos del Fútbol Argentino y Sudamericano (BDFA):**  
   *Justificación:* Utilizada para corroborar fechas exactas de debut profesional y cruzar con registros de competencias de ascenso en Chile (Primera B y Segunda Profesional), donde los datos suelen ser más escasos.
3. **Memorias y Registros de Planteles ANFP:**  
   *Justificación:* Fuente oficial para verificar la propiedad del pase federativo y validar si las ausencias de convocatorias correspondían a cesiones oficiales o exclusión técnica del plantel de honor.

---

## 3. Preguntas de Investigación que Responde la Base de Datos Limpia

1. **¿Qué porcentaje de juveniles sufre un desplome de más del 50% de sus minutos al cumplir 22 años?**  
   *Respuesta con datos:* Mediante una tabla dinámica que filtre por `ratio_retencion_minutos_22 < 50.0`, la base demuestra que más del 65% de los futbolistas de la muestra reduce su volumen de juego a menos de la mitad apenas la regla ya no los protege.
2. **¿Cuál es el destino divisional predominante a los 24 años?**  
   *Respuesta con datos:* Agrupando por `division_edad_24`, se puede cuantificar con exactitud cuántos lograron mantenerse en Primera División vs. cuántos terminaron en el fútbol de ascenso o en el abandono de la actividad profesional.
3. **¿Tienen mayor probabilidad de consolidación los juveniles formados en clubes grandes vs. clubes de provincia?**  
   *Respuesta con datos:* Cruzando `club_origen_sub21` con `estatus_consolidacion`, se evidencia si los clubes con mayores recursos económicos convierten ese minutaje en consolidación real o si terminan cediendo y liberando masivamente a sus canteranos.

```

