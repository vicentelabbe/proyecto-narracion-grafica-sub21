# Análisis del diseño de la historia — El mito del abismo

**Sofía Carvajal y Vicente Labbé | COM-208 | Entrega 05**

## Concepto editorial

El diseño de nuestra webstory busca conectar el lenguaje visual del fútbol con el periodismo de datos. Queremos que la experiencia remita a una pizarra táctica y a una interfaz de análisis deportivo, sin perder la claridad de un reportaje periodístico. El rediseño conserva el contraste y el verde de la identidad anterior, pero introduce más espacio entre los elementos, jerarquías tipográficas marcadas y un fondo oscuro constante.

El título *El mito del abismo* condensa nuestra pregunta inicial: si existe una ruptura en las oportunidades de los futbolistas cuando dejan atrás los 21 años. La palabra «mito» invita a poner a prueba esa creencia, no a asumir que es falsa antes de analizar los datos. La bajada presenta el problema como una pregunta y evita anticipar una respuesta absoluta. La portada es tipográfica: el título funciona como elemento principal de identidad, acompañado de una cifra que delimita la muestra de seguimiento.

## Estructura narrativa y recorrido del usuario

Organizamos el relato en cinco capítulos. El recorrido propone avanzar desde una pregunta general hasta una interpretación basada en evidencia, alternando bloques narrativos con elementos interactivos.

| Capítulo | Función narrativa | Experiencia del lector |
|---|---|---|
| 01. Entrar no es lo mismo que quedarse | Presentar el conflicto entre acceso y continuidad | Conocer la hipótesis y la escala de la investigación |
| 02. Diez años, dos fuentes | Mostrar de dónde proviene la evidencia y sus límites | Explorar la cobertura, buscar jugadores y filtrar torneos |
| 03. El espacio que dan los equipos | Introducir la dimensión de los clubes | Comparar minutos dentro de una temporada |
| 04. Más datos, menos mitos | Contrastar la hipótesis con los casos observados | Alternar promedio y mediana y examinar la continuidad |
| 05. Qué sabemos y qué falta | Cerrar con transparencia metodológica | Consultar fuentes y comprender las limitaciones |

El botón de portada invita a comenzar el recorrido y el menú de capítulos permite volver a cualquier sección. La lectura principal es lineal, pero los filtros permiten una exploración no lineal dentro de los gráficos. Las explicaciones se sitúan junto a la información que interpretan para que el lector no tenga que consultar un manual externo.

## Crónica y decisiones de redacción

La redacción busca combinar la tensión narrativa del periodismo deportivo con la precisión que requieren los datos. Preferimos preguntas, titulares breves y verbos activos a encabezados exclusivamente técnicos. «Entrar no es lo mismo que quedarse» diferencia dos fenómenos que suelen confundirse: alcanzar el primer equipo y mantener participación en cancha. «Diez años, dos fuentes» introduce la reconstrucción de los registros, mientras que «El espacio que dan los equipos» traslada la pregunta al nivel de los clubes. «Más datos, menos mitos» prepara la revisión de la hipótesis inicial.

Los textos no repiten mecánicamente todas las cifras de los gráficos. Introducen la pregunta, orientan la lectura y explican qué permite concluir la evidencia. La conclusión reconoce que los casos completos no representan necesariamente a quienes desaparecen de las bases. Conservamos la crónica anterior como antecedente del proceso y evitamos atribuir a los clubes intenciones que los minutos por sí solos no permiten demostrar.

## Identidad visual

| Elemento | Decisión | Función comunicativa |
|---|---|---|
| Fondo | Negro casi puro `#050505` | Evocar el entorno nocturno del estadio y dar continuidad al relato |
| Acento | Verde fosforescente `#C6FF36` | Vincular la identidad con la cancha y destacar cifras, controles y elementos activos |
| Texto principal | Blanco hueso `#F5F5F0` | Facilitar la lectura de textos extensos sin saturar de verde la pantalla |
| Texto secundario | Gris claro | Diferenciar notas, fuentes y aclaraciones de los titulares |
| Titulares | Anton, condensada y gruesa | Remitir a la gráfica deportiva y establecer jerarquía editorial |
| Cuerpo y controles | IBM Plex Mono, con fuentes alternativas | Evocar una terminal de datos y reforzar la relación entre análisis y fútbol |
| Tarjetas, bordes y retícula | Módulos oscuros y líneas finas | Separar capítulos y ordenar los gráficos sin introducir ruido visual |

El espacio en blanco —en este caso, espacio oscuro— ayuda a distinguir el cambio de capítulo y evita que los gráficos compitan entre sí. Utilizamos etiquetas directas, leyendas y explicaciones para que el color no sea el único recurso de interpretación. Los bocetos de referencia incluían fotografías de futbolistas; la beta publicada en los archivos del proyecto opta por una portada tipográfica y no presenta esas imágenes como material documental.

## De las entregas anteriores a la implementación

La hipótesis y las visualizaciones individuales construidas durante el semestre son el punto de partida del relato. Los perfiles de persona, mapa de viaje, wireframe e identidad visual elaborados en la Entrega 04 se conservan en [recursos](recursos/). La estructura actual traduce esos antecedentes a una experiencia navegable: portada, capítulos, navegación, módulos gráficos y cierre metodológico. El rediseño es una evolución de la propuesta anterior, no una sustitución de la investigación.

| Insumo | Traducción a la beta |
|---|---|
| Hipótesis y datos | Secuencia narrativa y comparación de minutos a distintas edades |
| Visualizaciones de la Entrega 03 | Comparación interactiva de clubes y seguimiento de casos completos |
| Wireframe | Organización de capítulos y jerarquía de los bloques |
| Perfiles y mapa de viaje | Recorrido guiado con opciones de exploración autónoma |
| Identidad visual | Sistema de colores, tipografía y componentes aplicado en CSS |

Los recursos originales están disponibles en [Identidad visual](recursos/Identidad%20visual.pdf), [Mapa de viaje](recursos/Mapa%20de%20viaje.pdf), [Perfiles de persona](recursos/Perfiles%20de%20persona.pdf) y [Wireframe y prototipo](recursos/Wireframe_prototipo.pdf).

## Comportamiento esperado y desarrollo técnico

El HTML contiene la estructura semántica y los textos; el CSS define la identidad, los espacios, la jerarquía y el comportamiento responsive; JavaScript controla los filtros, el buscador y los gráficos Plotly. Los datos se cargan localmente desde `data.js`. En pantallas estrechas las columnas se reorganizan verticalmente, los controles se adaptan al ancho disponible y la tabla puede desplazarse horizontalmente dentro de su contenedor.

## Plan de revisión de la beta

Antes de cerrar esta etapa, debemos comprobar la legibilidad en celular, iPad y computador; el funcionamiento de los enlaces y controles; la correspondencia entre los datos y las etiquetas; y la comprensión del recorrido por parte de lectores externos. La revisión de la versión publicada y sus resultados se registrarán en `pruebas_tecnicas.md`. También queda abierta la posibilidad de incorporar material fotográfico propio o autorizado en una futura versión, siempre que aporte a la historia.
