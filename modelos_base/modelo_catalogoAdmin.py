import mysql.connector

class RegistrarProductos:
    def __init__(self):
        # Conexión a la base de datos
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="proyecto_base"
        )
        self.cursor = self.conexion.cursor()

    def registrar_producto(self, producto):
        try:
            self.cursor.execute(
                "INSERT INTO productos (ID, nombre_productos, cantidad_productos, cantidad_ventas, categoria) VALUES (%s, %s, %s, %s, %s)",
                (producto.getId(), producto.getNombre(), producto.getStock(), producto.getVenta(), producto.getCategoria())
            )
            self.conexion.commit()
            return True
        except mysql.connector.Error as error:
            print(f"Error al registrar producto: {error}")
            self.conexion.rollback()
            return False

    def obtener_productos(self):
        consulta = "SELECT * FROM productos"
        self.cursor.execute(consulta)
        resultado = self.cursor.fetchall()
        return resultado


    def obtener_productos_por_categoria(self, categoria):
        consulta = "SELECT * FROM productos WHERE categoria = %s"
        self.cursor.execute(consulta, (categoria,))
        resultado = self.cursor.fetchall()
        return resultado


    def editar_producto(self, producto):
        try:
            self.cursor.execute(
                "UPDATE productos SET nombre_productos=%s, cantidad_productos=%s, cantidad_ventas=%s, categoria=%s WHERE ID=%s",
                (producto.getNombre(), producto.getStock(), producto.getVenta(), producto.getCategoria(), producto.getId())
            )
            self.conexion.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conexion.rollback()
            return False


    def eliminar_producto(self, id_producto):
        try:
            self.cursor.execute("DELETE FROM productos WHERE ID = %s", (id_producto,))
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

