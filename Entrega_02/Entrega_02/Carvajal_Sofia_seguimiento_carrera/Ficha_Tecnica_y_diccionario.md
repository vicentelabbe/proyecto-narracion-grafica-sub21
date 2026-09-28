# Ficha Técnica y Diccionario de Datos: Continuidad de Carrera Post-Regla Sub-21

## 1. Ficha Técnica

* **Fuente de los datos:** Registros históricos de trayectorias profesionales en [Transfermarkt](https://www.transfermarkt.es/), cotejados con bases de datos de [BDFA](https://www.bdfa.com.ar/) y memorias anuales de planteles publicadas por la Asociación Nacional de Fútbol Profesional (ANFP).
* **Metodología de construcción:** Levantamiento longitudinal por cohortes cerradas (camadas debutantes entre 2016 y 2021). Se identificó a cada futbolista que superó el umbral de 450 minutos jugados bajo el estatus Sub-21 en Primera División y se rastreó su actividad competitiva formal dos y cuatro años después (edades biológicas de 22 y 24 años).
* **Alcance de los datos:** 180 futbolistas chilenos que completaron su ciclo juvenil reglamentario en clubes de Primera División entre 2016 y 2021, garantizando una ventana de observación post-regla hasta el año 2024.
* **Características de los datos:** Dataset estructurado en formato tabular delimitado por comas (`.csv`), con codificación UTF-8. Cada registro corresponde al seguimiento individual y longitudinal de la carrera de un futbolista.
* **Otras observaciones:** En los casos de futbolistas que salieron a préstamo a ligas extranjeras formativas o filiales, se clasificó la división según la equivalencia jerárquica del país de destino.

---

## 2. Diccionario de Datos

| Variable | Descripción | Tipo de dato | Valores posibles / Rango | Observaciones editoriales |
| :--- | :--- | :--- | :--- | :--- |
| `id_jugador` | Identificador alfanumérico único del futbolista | String | Ej: `CHI-1001` | Clave foránea para cruzar con la base de minutaje |
| `nombre_jugador` | Nombre y apellido del futbolista | String | Texto libre | Normalizado sin caracteres especiales corruptos |
| `temporada_debut_sub21` | Año en que sumó por primera vez más de 450 min Sub-21 | Integer | `2016` a `2021` | Define la cohorte de seguimiento temporal |
| `club_origen_sub21` | Club con el que sumó la cuota juvenil | String | Nombres estandarizados de clubes chilenos | Club formador o empleador en etapa juvenil |
| `minutos_temporada_sub21` | Minutos totales sumados en su mejor temporada Sub-21 | Integer | `450` a `2700` | Volumen de rodaje previo al límite etario |
| `minutos_edad_22` | Minutos oficiales jugados a los 22 años cumplidos | Integer | `0` a `2700` | Mide la continuidad inmediata sin la regla |
| `division_edad_22` | Categoría competitiva en la que jugó a los 22 años | Categorical | `Primera Division`, `Primera B`, `Segunda Division`, `Extranjero`, `Sin Club/Retirado` | Mide descenso de categoría o consolidación |
| `minutos_edad_24` | Minutos oficiales jugados a los 24 años cumplidos | Integer | `0` a `2700` | Mide la maduración a mediano plazo |
| `division_edad_24` | Categoría competitiva en la que jugó a los 24 años | Categorical | `Primera Division`, `Primera B`, `Segunda Division`, `Extranjero`, `Sin Club/Retirado` | Mide consolidación profesional plena |
| `ratio_retencion_minutos_22` | Porcentaje de minutos a los 22 vs. temporada Sub-21 | Float | `0.0` a `200.0+` | Calculado: `(minutos_edad_22 / minutos_sub21) * 100` |
| `estatus_consolidacion` | Clasificación final de la carrera post-regla | Categorical | `Consolidado Primera`, `Exportado`, `Descendido`, `Estancado/Sin Club` | Indicador sintético para gráficos y visualización |
