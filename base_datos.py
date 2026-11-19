import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect("monitoreo.db")

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            frecuencia_cardiaca INTEGER,
            spo2 INTEGER,
            frecuencia_respiratoria INTEGER,
            temperatura REAL,
            presion_sistolica INTEGER,
            presion_diastolica INTEGER
        )
    """)

    conexion.commit()
    conexion.close()

def guardar_registro(fc, spo2, fr, temp, pas, pad):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO registros (
            fecha, frecuencia_cardiaca, spo2,
            frecuencia_respiratoria, temperatura,
            presion_sistolica, presion_diastolica
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        fc, spo2, fr, temp, pas, pad
    ))

    conexion.commit()
    conexion.close()

def consultar_registros():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM registros ORDER BY id DESC")
    datos = cursor.fetchall()

    conexion.close()
    return datos

crear_tabla()