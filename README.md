# Análisis Logístico y Reducción de Merma en Exportación de Banano (Urabá)

![Dashboard Preview](dashboard/dashboard_screenshot.png)

## Resumen del Proyecto
Este proyecto de análisis de datos busca identificar los cuellos de botella operativos que aumentan el porcentaje de cajas de banano rechazadas en los puertos de Urabá (Carepa, Turbo, Chigorodó, Apartadó). A través de un proceso ETL y modelado de datos, se detectaron los factores que generan mayores pérdidas económicas por madurez prematura.

## Herramientas Utilizadas
* **Python (Pandas, NumPy):** Extracción, limpieza de datos nulos y estandarización de formatos (ETL).
* **PostgreSQL:** Almacenamiento, consultas avanzadas (CTEs, Window Functions) para generar rankings de rendimiento por finca.
* **Power BI & DAX:** Modelado de datos (Esquema de Estrella) y visualización interactiva de KPIs.

## Metodología (El Pipeline)
1. **Recolección de Datos:** Simulación de 1,500 registros logísticos usando un script de Python.
2. **Limpieza (Data Cleaning):** Manejo de valores nulos (imputación de promedios en horas de tránsito) y corrección de inconsistencias tipográficas mediante Pandas (`notebooks/01_data_cleaning_and_eda.ipynb`).
3. **Análisis Exploratorio (SQL):** Identificación del Top 5 de rutas logísticas con mayor índice de rechazo (`sql_scripts/02_analysis_queries.sql`).
4. **Visualización:** Desarrollo de un dashboard gerencial enfocado en el cálculo de pérdidas económicas ($) y % de merma.

## Insights y Recomendaciones de Negocio
1. **El Problema del Turno PM:** Los envíos originados en Turbo durante el turno de la tarde (12 PM - 8 PM) con tiempos de tránsito superiores a 4 horas incrementan la merma por "Madurez Prematura" en un 18%.
2. **Impacto Económico:** Las 3 fincas con peor rendimiento en la ruta de Chigorodó representan el 45% del total de pérdidas económicas del mes.
3. **Recomendación Logística:** Restringir los despachos de las zonas alejadas (Turbo/Chigorodó) exclusivamente a los turnos de madrugada (4 AM - 12 PM) para reducir la exposición al calor y bajar la pérdida económica mensual proyectada en un 12%.

## Cómo ejecutar este proyecto
1. Clona el repositorio: `git clone https://github.com/tu-usuario/uraba-agro-logistics-analysis.git`
2. Instala las dependencias de Python: `pip install pandas numpy`
3. Ejecuta el notebook de Jupyter para procesar los datos o abre el archivo `.pbix` en Power BI Desktop.
