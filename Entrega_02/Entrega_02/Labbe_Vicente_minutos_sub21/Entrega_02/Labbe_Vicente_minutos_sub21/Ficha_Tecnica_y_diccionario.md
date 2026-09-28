# Ficha Técnica y Diccionario de Datos: Minutaje Sub-21 en Primera División

## 1. Ficha Técnica

* **Fuente de los datos:** Planillas oficiales de juego y actas referiles publicadas por la Asociación Nacional de Fútbol Profesional (ANFP) a través del portal oficial [Campeonato Chileno](https://campeonatochileno.cl/), complementadas y contrastadas con bases estructuradas de [Soccerway](https://es.soccerway.com/) y [Transfermarkt](https://www.transfermarkt.es/).
* **Metodología de construcción:** Consolidación de registros partido a partido de las temporadas 2016 a 2024. Se fusionaron las planillas de alineación con el registro de sustituciones y goles, calculando el minutaje efectivo de participación juvenil por encuentro y agregándolo por jugador y club.
* **Alcance de los datos:** Primera División del fútbol masculino profesional de Chile, abarcando 9 temporadas regulares completas (2016–2024). Incluye a todos los futbolistas que cumplieron con la condición etaria Sub-20/Sub-21 según las bases del torneo de cada año respectivo.
* **Características de los datos:** Archivo estructurado tabular en formato delimitado por comas (`.csv`), con codificación UTF-8. Cada fila representa el agregado estacional de un futbolista juvenil en un club específico durante una temporada regular.
* **Otras observaciones:** Se descartaron los minutos adicionados por tiempo de descuento, ciñéndose al estándar reglamentario oficial de 90 minutos por partido utilizado por la ANFP para el cómputo de la regla.

---

## 2. Diccionario de Datos

| Variable | Descripción | Tipo de dato | Valores posibles / Rango | Observaciones editoriales |
| :--- | :--- | :--- | :--- | :--- |
| `id_jugador` | Identificador único alfanumérico del futbolista | String | Ej: `CHI-1001` | Clave primaria para cruce con bases de cohortes y transferencias |
| `nombre_jugador` | Nombre y apellido oficial del deportista | String | Texto libre | Normalizado sin caracteres especiales corruptos ni apodos |
| `club` | Club en el que disputó la temporada | String | Nombres estandarizados (16 clubes Primera División) | Se unificaron variantes de nombres societarios (ej. *Colo-Colo*) |
| `temporada` | Año calendario del campeonato | Integer | `2016` a `2024` | Torneos anuales y de transición homologados |
| `edad_en_temporada`| Edad del jugador al 31 de diciembre del año del torneo | Integer | `15` a `21` | Permite segmentar el cumplimiento por rango precoz vs. límite |
| `posicion_agrupada`| Zona principal de desempeño táctico | Categorical | `Arquero`, `Defensa`, `Mediocampista`, `Delantero` | Homologado desde 14 roles específicos hacia 4 cuadrantes |
| `partidos_convocado`| Encuentros en los que formó parte de la nómina | Integer | `0` a `30` | Mide presencia general en el primer equipo |
| `partidos_titular` | Encuentros en los que integró el once inicial | Integer | `0` a `30` | Mide respaldo táctico desde el arranque |
| `partidos_sustituido`| Encuentros en que inició de titular pero fue reemplazado | Integer | `0` a `30` | Clave para evaluar sustituciones tempranas |
| `minuto_promedio_salida`| Minuto medio del partido en el que fue reemplazado | Float | `1.0` a `90.0` (o `0.0` si no fue sustituido) | Evidencia si los cambios ocurren al entretiempo |
| `minutos_sub21_regla` | Minutos válidos aportados al cómputo de la regla | Integer | `0` a `1350` | Aplica el tope máximo por partido fijado por bases ANFP |
| `minutos_totales_liga` | Minutos totales en cancha durante el campeonato | Integer | `0` a `2700` | Permite contrastar participación total vs. minutos regla |
| `cuota_completada_club`| Si el club cumplió el 70% reglamentario en ese torneo | Boolean | `True`, `False` | Variable de contexto institucional |
