# Documentación Metodológica y Proceso de Visualización - Integrante 02: Sofía Carvajal

## 1. Proceso de Diseño Visual en Altair y Decisiones Tomadas

Para comunicar la disparidad institucional en la aplicación de la norma juvenil en 2019, se diseñó un gráfico de barras ordenadas (*ranked bar chart*) interactivo en Altair:

* **Orientación y Ejes:**  
  * Eje Y (`club`): Presenta los 16 clubes ordenados de forma descendente por minutaje, permitiendo una lectura jerárquica instantánea de mayor a menor compromiso formativo.
  * Eje X (`minutos_sub21`): Representa el volumen cuantitativo de rodaje otorgado.
* **Línea de Referencia Normativa:** Se incorporó una marca de regla punteada vertical en los 1.350 minutos (color `#D55E00`), que visibiliza la línea de flotación reglamentaria de la ANFP. Esto permite distinguir visualmente a los clubes que superaron la norma por convicción deportiva de aquellos que detuvieron la rotación apenas cumplieron la cuota.
* **Canal de Color:** Codifica la variable `posicion_predominante` utilizando la paleta accesible Okabe-Ito (Azul `#0072B2` para Volantes, Amarillo/Naranja `#E69F00` para Laterales y Verde `#009E73` para Delanteros), revelando que los equipos con menor minutaje tendieron a utilizar posiciones de menor riesgo directo en el arco propio.
* **Tooltips de Exploración:** Permiten inspeccionar el desglose posicional exacto de minutos y el número de canteranos utilizados por institución.

## 2. Base de Datos Utilizada y Procesamiento

* **Fuente seleccionada:** `minutos_sub21_clubes_2019.csv` (16 filas).  
* **Justificación:** Resume el comportamiento global de la Primera División en el mismo año basal analizado en la visualización individual 01 (cohorte 2019), permitiendo conectar el destino de los jugadores con la cultura formativa de los clubes de origen.

## 3. Preguntas que Responde la Visualización

1. **¿Existe un cumplimiento uniforme de la regla Sub-21 entre los clubes de Primera División?**  
   *No: existe una brecha de más de 2.200 minutos entre los clubes formadores (Colo-Colo, O'Higgins, Huachipato) y los clubes que se mantuvieron al borde del descenso administrativo.*
2. **¿En qué posiciones del campo deciden los cuerpos técnicos cumplir con el minutaje juvenil?**  
   *La gran mayoría concentra sus minutos en volantes y laterales, minimizando la rotación en puestos de alta vulnerabilidad como la portería o la zaga central.*