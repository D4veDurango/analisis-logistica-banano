
# Análisis Logístico y Reducción de Merma en la Exportación de Banano — Urabá

## Dashboard en Power BI


## Descripción del proyecto

Este proyecto busca analizar el comportamiento de las operaciones logísticas relacionadas con la exportación de banano en la región de Urabá, Antioquia, Colombia.

El objetivo es identificar patrones asociados al rechazo de cajas de banano y explorar cómo variables como el municipio de origen, el turno de despacho y el tiempo de tránsito pueden relacionarse con los niveles de merma.

**Nota:** El conjunto de datos utilizado es sintético y fue generado mediante Python con fines educativos y de demostración. Los resultados no representan cifras reales de empresas o exportaciones de la región.

## Objetivos

- Explorar los factores asociados al rechazo de cajas de banano.
- Identificar diferencias entre municipios y turnos de despacho.
- Analizar la relación entre los tiempos de tránsito y los porcentajes de rechazo.
- Construir indicadores que faciliten la interpretación de la operación logística.
- Presentar los resultados mediante un dashboard interactivo en Power BI.

## Herramientas utilizadas

| Herramienta | Aplicación |
|---|---|
| Python | Generación y procesamiento de datos |
| Pandas | Limpieza y transformación de datos |
| NumPy | Generación de datos sintéticos |
| Jupyter Notebook | Exploración y documentación del proceso |
| Power BI | Modelado y visualización de información |
| DAX | Construcción de indicadores y métricas |

## Datos utilizados

Se generó un conjunto de datos sintético de 1.500 registros que representa operaciones logísticas de banano en cuatro municipios:

- Carepa
- Apartadó
- Turbo
- Chigorodó

Entre las variables disponibles se encuentran:

- Municipio de origen.
- Tiempo de tránsito.
- Turno de despacho.
- Cantidad de cajas.
- Cantidad de cajas rechazadas.
- Motivo del rechazo.

## Metodología

El proyecto se desarrolla mediante las siguientes etapas:

1. **Generación de datos:** creación de registros sintéticos mediante Python.
2. **Inspección inicial:** revisión de la estructura, los valores nulos y las inconsistencias.
3. **Limpieza de datos:** corrección de errores tipográficos y tratamiento de valores faltantes mediante Pandas.
4. **Visualización:** utilización de Power BI para explorar los indicadores y patrones logísticos.

## Estructura del repositorio

```text
analisis-logistica-banano/
│
├── Dashboard.pbix
├── README.md
├── generador_datos.py
├── limpieza_datos.ipynb
├── logistica_banano_uraba.csv
└── logistica_limpia.csv
```

## Indicadores de análisis

El proyecto permite explorar diferentes indicadores, entre ellos:

- Porcentaje de rechazo de cajas.
- Cantidad de cajas transportadas y rechazadas.
- Comportamiento del rechazo por municipio.
- Distribución de los despachos por turno.
- Relación entre el tiempo de tránsito y el rechazo.

Los resultados deben interpretarse teniendo en cuenta que los datos son simulados.

## Resultados del análisis exploratorio

El análisis se realizó sobre un conjunto de datos sintético de 1.500 viajes de transporte de banano.

### 1. Rechazo por municipio

Se identificaron diferencias en las tasas de rechazo entre los municipios analizados:

| Municipio | Tasa de rechazo |
|---|---:|
| Turbo | 7.50% |
| Chigorodó | 5.22% |
| Carepa | 3.43% |
| Apartadó | 3.39% |

Turbo presentó la mayor tasa de rechazo, por lo que representa un punto de interés para futuras investigaciones.

### 2. Rechazo por turno

| Turno | Tasa de rechazo |
|---|---:|
| Tarde | 6.92% |
| Noche | 4.02% |
| Mañana | 3.98% |

El turno de la tarde presentó una tasa de rechazo superior a los otros dos turnos.

### 3. Rechazo según tiempo de tránsito

| Tiempo de tránsito | Tasa de rechazo |
|---|---:|
| Hasta 2 horas | 3.46% |
| Más de 2 a 4 horas | 3.32% |
| Más de 4 a 6 horas | 8.31% |
| Más de 6 horas | 8.60% |

Los viajes con tiempos de tránsito superiores a cuatro horas presentaron tasas de rechazo más altas en el conjunto de datos.

### 4. Calidad de los datos

Se identificaron 45 registros sin información de horas de tránsito, equivalentes al 3% del conjunto de datos.

La tasa de rechazo fue de 4.92% en los registros completos y de 4.82% en los registros sin información de tránsito.

Los valores faltantes se conservaron para evitar introducir información no disponible.

**Nota:** Estos resultados corresponden a datos sintéticos y tienen fines educativos. Las relaciones observadas no demuestran causalidad ni representan necesariamente el comportamiento real de las operaciones bananeras.

## Mejoras futuras

- Ampliar el análisis exploratorio de datos (EDA).
- Incorporar consultas SQL para análisis y segmentación.
- Evaluar diferentes estrategias de tratamiento de valores faltantes.
- Analizar el impacto económico de las cajas rechazadas.
- Mejorar la reproducibilidad del proceso de generación de datos.
- Validar hipótesis mediante análisis estadístico.

## Cómo explorar el proyecto

1. Consulta `logistica_banano_uraba.csv` para revisar los datos originales.
2. Revisa `generador_datos.py` para conocer cómo se crearon los registros.
3. Abre `limpieza_datos.ipynb` para consultar el proceso de limpieza.
4. Consulta `logistica_limpia.csv` para revisar los datos procesados.
5. Abre `Dashboard.pbix` con Power BI Desktop para explorar las visualizaciones.

---

**Proyecto de portafolio — Data Analytics**

Enfoque: análisis de datos, limpieza, exploración y visualización.
