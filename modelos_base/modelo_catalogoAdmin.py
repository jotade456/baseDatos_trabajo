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
        except mysql.connector.Error as error:
            print(f"Error: {error}")
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
    
    def editar_productos(self,ID, nombre,cantidad,ventas,categoria):
        try:
            self.cursor.execute(
                "UPDATE productos SET nombre_productos=%s, cantidad_productos=%s, cantidad_ventas=%s, categoria=%s WHERE ID=%s",
                (nombre, cantidad, ventas, categoria, ID)
            )
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conexion.rollback()
            return False

    def eliminar_producto(self, ID):
        try:
            self.cursor.execute("DELETE FROM productos WHERE ID = %s", (ID,))
            self.conexion.commit()

            if self.cursor.rowcount > 0:
                return True
            else:
                return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conexion.rollback()
            return False
    
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()