from vistas_base.vista_proyecto import Vista
from vistas_base.vista_catalogoAdmin import CatalogoApp
from vistas_base.vista_catalogoUsuario import CatalogoUsuario
from modelos_base.modelo_proyecto import conexion_BD
from modelos_base.modelo_catalogoAdmin import RegistrarProductos
from vistas_base.vista_registro import abrir_registro_producto
from modelos_base.modelo_json import crear_archivo_informe
from vistas_base.vista_informe import InformeProductos
from vistas_base.vista_editar import edicion
from vistas_base.vista_crearJson import Vista_json
from modelos_base.modelo_productos import Producto

class Controlador:
    def __init__(self):
        self.modelo = conexion_BD()
        self.modelo_catalogo = RegistrarProductos()
        self.vista = Vista(self)
        self.archivo_informe = crear_archivo_informe() 
        self.catalogoAdministrador = None
        self.catalogoUsuario = None
        self.registro_producto = None
        self.informe_vista=None
        self.ventana_edicion=None
        self.vistaJson=None
        self.productos= Producto()


    def enviar_datos(self, nombre, contraseña, rol):
        return self.modelo.verificar_datos(nombre, contraseña, rol)



    def verificar_usuario(self, rol):
        if rol == "Administrador":
            self.catalogoAdministrador = CatalogoApp(self)
            self.catalogoAdministrador.iniciar_catalogo()


        elif rol == "Usuario":
            self.catalogoUsuario = CatalogoUsuario(self)
            self.catalogoUsuario.iniciar_catalogo()



    def agregar_producto(self, id, nombre, stock, venta, categoria):
        self.productos.setId(id)
        self.productos.setNombre(nombre)
        self.productos.setStock(stock)
        self.productos.setVenta(venta)
        self.productos.setCategoria(categoria)

        return self.modelo_catalogo.registrar_producto(self.productos)



    def abrir_registro(self):
        self.registro_producto = abrir_registro_producto(self)
        self.registro_producto.iniciar_programa()



    def obtener_productos(self):
        return self.modelo_catalogo.obtener_productos()
    


    def obtener_productos_por_categoria(self, categoria):
        return self.modelo_catalogo.obtener_productos_por_categoria(categoria)
    
    def abrir_vista_json(self):
        self.vistaJson=Vista_json(self)
        self.vistaJson.abrirVista()

    
    def guardar_informe(self,nombreArchivo):
        productos = self.modelo_catalogo.obtener_productos()
        nombreArchivo=self.archivo_informe.crearArchivo(productos,nombreArchivo)
        return nombreArchivo


    def deserializar (self,nombreArchivo):
        texto=self.archivo_informe.deserializar(nombreArchivo)
        return texto
    


    def abrir_vista_informe(self):
        productos = self.modelo_catalogo.obtener_productos()
        self.informe_vista = InformeProductos(self, productos)
        self.informe_vista.iniciar_informe()


    def editar_productos(self, id, nombre, cantidad,ventas, categoria):
        self.productos.setId(id)
        self.productos.setNombre(nombre)
        self.productos.setStock(cantidad)
        self.productos.setVenta(ventas)
        self.productos.setCategoria(categoria)
        
        return self.modelo_catalogo.editar_producto(self.productos)


    def eliminar_producto_por_id(self, id_producto):
        return self.modelo_catalogo.eliminar_producto(id_producto)


    def abrir_edicion(self):
        self.ventana_edicion=edicion(self)
        self.ventana_edicion.iniciar_programa()
        


    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
        self.modelo_catalogo.cerrar_conexion()
        


    def iniciar_programa(self):
        self.vista.iniciar_vista()
