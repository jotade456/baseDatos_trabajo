import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class CatalogoUsuario:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Toplevel() 
        self.root.title("Catálogo de Productos")
        self.root.geometry("800x600")  
        self.crear_componentes()
        self.mostrar_productos()
        self.actualizar_periodicamente()

    def crear_componentes(self):
        marco_superior = tk.Frame(self.root, bd=2, relief="groove")
        marco_superior.pack(fill="x")

        nombre_empresa = tk.Label(marco_superior, text="NexusPlay Studios", font=("Arial", 16))
        nombre_empresa.pack(side="left", padx=10, pady=10)

        logo = tk.Label(marco_superior, text="Logo", font=("Arial", 12), bg="gray", width=10, height=5)
        logo.pack(side="right", padx=10, pady=10)

        
        barra_nav = tk.Frame(self.root, bd=2, relief="groove")
        barra_nav.pack(fill="x")

        marco_categorias = tk.Frame(self.root, bd=2, relief="groove")
        marco_categorias.pack(fill="x")

        
        self.crear_botones_acciones(marco_categorias)

        titulo_catalogo = tk.Label(self.root, text="Catálogo de Productos", font=("Arial", 14))
        titulo_catalogo.pack(pady=10)

        
        self.frame_catalogo = tk.Frame(self.root)
        self.frame_catalogo.pack(pady=10)
        
        
        

    def crear_botones_acciones(self, marco_categorias):
        acciones = ["Ver informe productos", "Soporte y Contacto"]
        for accion in acciones:
            btn_categoria = tk.Button(marco_categorias, text=accion, command=lambda c=accion: self.boton_accion(c))
            btn_categoria.pack(side="left", padx=10, pady=10)

    def boton_accion(self, accion):
        if accion == "Ver informe productos":
            self.controlador.abrir_vista_informe()
        elif accion == "Soporte y Contacto":
            pass


    def filtrar_por_categoria(self):
        categoria = simpledialog.askstring("Filtrar por Categoría", "Ingrese la categoría para filtrar:")
        if categoria:
            self.mostrar_productos(categoria)

    def mostrar_productos(self, categoria=None):
        for child in self.frame_catalogo.winfo_children():
            child.destroy()

        productos = self.controlador.modelo_catalogo.obtener_productos(categoria)
        for producto in productos:
            cuadro_producto = tk.Frame(self.frame_catalogo, bd=2, relief="groove", padx=10, pady=10)
            cuadro_producto.pack(side="left", padx=10)

            tk.Label(cuadro_producto, text=f"ID: {producto[0]}").pack()
            tk.Label(cuadro_producto, text=f"Nombre: {producto[1]}").pack()
            tk.Label(cuadro_producto, text=f"Cantidad: {producto[2]}").pack()
            tk.Label(cuadro_producto, text=f"Ventas: {producto[3]}").pack()
            tk.Label(cuadro_producto, text=f"Categoría: {producto[4]}").pack()

    def actualizar_catalogo(self):
        self.mostrar_productos()
        

    def actualizar_periodicamente(self):
        self.actualizar_catalogo()
        self.root.after(30000, self.actualizar_periodicamente)

    def iniciar_catalogo(self):
        self.root.mainloop()