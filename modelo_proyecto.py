import json
import mysql.connector
class conexion_BD:
    def __init__(self):
        self.conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="proyecto_base"
        )
        self.cursor=self.conexion.cursor()
    def verificar_datos(self,nombre,contraseña,rol):
        consulta = "SELECT COUNT(*) FROM usuario WHERE nombre = %s AND contraseña = %s AND rol = %s"
        self.cursor.execute(consulta, (nombre, contraseña, rol))
        resultado = self.cursor.fetchone()
        return resultado[0] > 0 
        
        
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()