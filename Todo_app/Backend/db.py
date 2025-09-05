import mysql.connector
from mysql.connector import Error

def get_connection():
    """Crea y devuelve una conexión a la base de datos MySQL."""
    try:
        connection = mysql.connector.connect(
            host="localhost",      # Cambiar si usas otro host
            user="root",           # Tu usuario de MySQL
            password="tu_password",# Cambiar por tu contraseña
            database="todo_app"    # Nombre de la base de datos
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None

def get_cursor_dict():
    """Devuelve un cursor con formato diccionario para consultas."""
    conn = get_connection()
    if conn:
        return conn, conn.cursor(dictionary=True)
    else:
        return None, None