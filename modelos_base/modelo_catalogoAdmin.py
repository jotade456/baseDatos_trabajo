import mysql.connector
class registrar_producto:
    def __init__(self):
        self.conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="proyecto_base"
        )
        self.cursor=self.conexion.cursor()
        
        
    def registrar_datosProducto(self, ID, nombre, cantidad, ventas, categoria):
        try:
            self.cursor.execute(
                "INSERT INTO productos (ID, nombre_productos, cantidad_productos, cantidad_ventas, categoria) VALUES (%s, %s, %s, %s, %s)",
                (ID, nombre, cantidad, ventas, categoria)
            )
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conexion.rollback()
            return False

    def obtener_productos(self, categoria=None):
        if categoria:
            consulta = "SELECT * FROM productos WHERE categoria = %s"
            self.cursor.execute(consulta, (categoria,))
        else:
            consulta = "SELECT * FROM productos"
            self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        return resultado


        
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()