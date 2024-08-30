class Controlador:
    def __init__(self):
        self.modelo = conexion_BD()
        self.vista = Vista(self)

    def verificar_usuario(self, nombre, contraseña, rol):
        return self.modelo.verificar_datos(nombre, contraseña, rol)
    
    def cerrar_conexion(self):
        self.modelo.cerrar_conexion()
        
    def iniciar_programa(self):
        self.vista.iniciar_vista()

if __name__ == "__main__":
    objControlador = Controlador()
    objControlador.iniciar_programa()
