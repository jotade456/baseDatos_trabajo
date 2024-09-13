from vistas_base.vista_proyecto import Vista
from vistas_base.vista_catalogoAdmin import CatalogoApp
from vistas_base.vista_catalogoUsuario import CatalogoUsuario
from modelos_base.modelo_proyecto import conexion_BD
from modelos_base.modelo_catalogoAdmin import registrar_producto
from vistas_base.vista_registro import abrir_registro_producto
from modelos_base.modelo_json import crear_archivo_informe
from vistas_base.vista_informe import InformeProductos
from vistas_base.vista_editar import edicion

class Controlador:
    def __init__(self):
        self.modelo = conexion_BD()
        self.modelo_catalogo = registrar_producto()
        self.vista = Vista(self)
        self.archivo_informe = crear_archivo_informe() 
        self.catalogoAdministrador = None
        self.catalogoUsuario = None
        self.registro_producto = None
        self.informe_vista=None
        self.ventana_edicion=None

    def enviar_datos(self, nombre, contraseña, rol):
        return self.modelo.verificar_datos(nombre, contraseña, rol)

    def verificar_usuario(self, rol):
        if rol == "Administrador":
            self.catalogoAdministrador = CatalogoApp(self)
            self.catalogoAdministrador.iniciar_catalogo()
        elif rol == "Usuario":
            self.catalogoUsuario = CatalogoUsuario(self)
            self.catalogoUsuario.iniciar_catalogo()

    def agregar_producto(self, ID, nombre, cantidad, ventas, categoria):
        resultado = self.modelo_catalogo.registrar_datosProducto(ID, nombre, cantidad, ventas, categoria)
        if resultado and self.catalogoAdministrador:
            self.catalogoAdministrador.actualizar_catalogo()
        return resultado

    def abrir_registro(self):
        self.registro_producto = abrir_registro_producto(self)
        self.registro_producto.iniciar_programa()
        
    def obtener_productos(self, categoria):
        return self.modelo_catalogo.obtener_productos(categoria)
    
    def guardar_informe(self):
        productos = self.modelo_catalogo.obtener_productos()
        self.archivo_informe.crearArchivo(productos, "informe_productos")

    
    def cargar_informe(self):
        datos_deserializados = self.archivo_informe.deserializar("informe_productos")
        return datos_deserializados

    def abrir_vista_informe(self):
        productos = self.modelo_catalogo.obtener_productos()
        self.informe_vista = InformeProductos(self, productos)
        self.informe_vista.iniciar_informe()

    def editar_productos(self, id, nombre, cantidad,ventas, categoria):
        return self.modelo_catalogo.editar_productos(id, nombre, cantidad,ventas, categoria)
    
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