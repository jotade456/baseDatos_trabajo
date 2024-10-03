import tkinter as tk
from tkinter import ttk

class CatalogoUsuario:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Toplevel()
        self.root.title("Catálogo de Productos - NexusPlay Studios")
        self.root.geometry("850x650")
        self.root.configure(bg="#f0f0f0")
        self.crear_componentes()
        self.mostrar_productos()
        self.actualizar_periodicamente()

    def crear_componentes(self):
        marco_superior = tk.Frame(self.root, bg="#4682b4", bd=2, relief="groove")
        marco_superior.pack(fill="x")

        nombre_empresa = tk.Label(marco_superior, text="NexusPlay Studios", font=("Arial", 20, "bold"), bg="#4682b4", fg="white")
        nombre_empresa.pack(side="left", padx=20, pady=15)

        logo = tk.Label(marco_superior, text="Logo", font=("Arial", 14), bg="white", fg="black", width=10, height=5)
        logo.pack(side="right", padx=20, pady=10)

        barra_nav = tk.Frame(self.root, bg="#87CEEB", bd=2, relief="groove")
        barra_nav.pack(fill="x", padx=20, pady=5)

        titulo_catalogo = tk.Label(self.root, text="Catálogo de Productos", font=("Arial", 16, "bold"), bg="#f0f0f0")
        titulo_catalogo.pack(pady=15)

        self.frame_catalogo = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_catalogo.pack(pady=10)

    def mostrar_productos(self):
        for child in self.frame_catalogo.winfo_children():
            child.destroy()

        productos = self.controlador.modelo_catalogo.obtener_productos()

        for producto in productos:
            cuadro_producto = tk.Frame(self.frame_catalogo, bd=2, relief="groove", padx=10, pady=10, bg="#ffffff")
            cuadro_producto.pack(side="left", padx=10, pady=10)

            tk.Label(cuadro_producto, text=f"ID: {producto[0]}", font=("Arial", 12, "bold")).pack(anchor="w")
            tk.Label(cuadro_producto, text=f"Nombre: {producto[1]}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(cuadro_producto, text=f"Cantidad: {producto[2]}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(cuadro_producto, text=f"Ventas: {producto[3]}", font=("Arial", 12)).pack(anchor="w")
            tk.Label(cuadro_producto, text=f"Categoría: {producto[4]}", font=("Arial", 12)).pack(anchor="w")

    def actualizar_catalogo(self):
        self.mostrar_productos()

    def actualizar_periodicamente(self):
        self.actualizar_catalogo()
        self.root.after(9000, self.actualizar_periodicamente)

    def iniciar_catalogo(self):
        self.root.mainloop()
