
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Los datos generados son simulados y no representan operaciones reales.

np.random.seed(42)
random.seed(42)

num_registros = 1500

municipios = ['Carepa', 'Apartadó', 'Turbo', 'Chigorodó']
fincas_base = ['La Esperanza', 'El Bananal', 'Villa Verde', 'San José', 'La Bonita', 'El Tesoro']
empresas_transporte = ['TransUrabá', 'Logística Bananera', 'Rutas del Darién', 'Carga Agrícola S.A.']
motivos_rechazo = ['Madurez Prematura', 'Daño Mecánico', 'Calibre No Conforme', 'Cicatriz/Mancha']
turnos = ['Mañana (4am-12pm)', 'Tarde (12pm-8pm)', 'Noche (8pm-4am)']

datos = []
fecha_inicio = datetime(2025, 1, 1)

for i in range(num_registros):
    id_viaje = f"V-{10000 + i}"
    fecha_envio = fecha_inicio + timedelta(days=random.randint(0, 180))
    municipio = random.choice(municipios)
    finca = f"{random.choice(fincas_base)} {municipio}"
    transporte = random.choice(empresas_transporte)
    turno = random.choice(turnos)

    cajas_enviadas = random.randint(800, 1100)

    if municipio == 'Turbo':
        horas_transito = round(random.uniform(3.5, 6.5), 1)
    elif municipio == 'Chigorodó':
        horas_transito = round(random.uniform(2.5, 5.0), 1)
    else:
        horas_transito = round(random.uniform(1.0, 3.0), 1)

    tasa_rechazo_base = random.uniform(0.01, 0.04)

    if turno == 'Tarde (12pm-8pm)':
        tasa_rechazo_base += 0.03

    if horas_transito > 4.0:
        tasa_rechazo_base += 0.05

    cajas_rechazadas = int(cajas_enviadas * tasa_rechazo_base)
    cajas_aprobadas = cajas_enviadas - cajas_rechazadas

    if horas_transito > 4.0 and turno == 'Tarde (12pm-8pm)':
        motivo = 'Madurez Prematura'
    else:
        motivo = random.choice(motivos_rechazo)

    datos.append([
        id_viaje,
        fecha_envio.strftime('%Y-%m-%d'),
        municipio,
        finca,
        transporte,
        turno,
        horas_transito,
        cajas_enviadas,
        cajas_aprobadas,
        cajas_rechazadas,
        motivo
    ])

columnas = [
    'id_viaje',
    'fecha_envio',
    'municipio_origen',
    'finca_origen',
    'empresa_transporte',
    'turno',
    'horas_transito',
    'cajas_enviadas',
    'cajas_aprobadas',
    'cajas_rechazadas',
    'motivo_rechazo_principal'
]

df_exportaciones = pd.DataFrame(datos, columns=columnas)

# Se agregan algunos valores faltantes y errores tipográficos para practicar limpieza.

indices_nulos = np.random.choice(
    df_exportaciones.index,
    size=45,
    replace=False
)

df_exportaciones.loc[indices_nulos, 'horas_transito'] = np.nan

indices_typos = np.random.choice(
    df_exportaciones.index,
    size=30,
    replace=False
)

typos_dict = {
    'Carepa': 'carepa ',
    'Apartadó': 'Apartado',
    'Turbo': 'TURBO',
    'Chigorodó': 'Chigorodo'
}

for idx in indices_typos:
    mun_actual = df_exportaciones.loc[idx, 'municipio_origen']
    df_exportaciones.loc[idx, 'municipio_origen'] = typos_dict.get(
        mun_actual,
        mun_actual
    )

nombre_archivo = 'logistica_banano_uraba.csv'

df_exportaciones.to_csv(
    nombre_archivo,
    index=False,
    encoding='utf-8'
)

print(f"Archivo '{nombre_archivo}' generado correctamente.")
print(f"Total de registros: {len(df_exportaciones)}")
print(f"Valores faltantes en horas de tránsito: {df_exportaciones['horas_transito'].isnull().sum()}")
print("El conjunto incluye errores tipográficos intencionales para practicar limpieza.")
