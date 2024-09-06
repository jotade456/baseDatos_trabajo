import tkinter as tk
from tkinter import ttk
class InformeProductos:
    def __init__(self, controlador, productos):
        self.controlador = controlador
        self.productos = productos
        self.root = tk.Toplevel()
        self.root.title("Informe de Productos")
        self.root.geometry("600x400")
        self.crear_componentes()

    def crear_componentes(self):
        tk.Label(self.root, text="Informe de Productos Registrados", font=("Arial", 14)).pack(pady=10)

        botones_frame = tk.Frame(self.root)
        botones_frame.pack(pady=10)
        
        tk.Button(botones_frame, text="Más Vendidos", command=self.mostrar_mas_vendidos).pack(side="left", padx=10)
        tk.Button(botones_frame, text="Menos Vendidos", command=self.mostrar_menos_vendidos).pack(side="left", padx=10)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Cantidad", "Ventas", "Categoría"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Cantidad", text="Cantidad")
        self.tree.heading("Ventas", text="Ventas")
        self.tree.heading("Categoría", text="Categoría")
        self.tree.pack(fill="both", expand=True)

        self.mostrar_productos(self.productos)

    def mostrar_productos(self, productos):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for producto in productos:
            self.tree.insert("", "end", values=producto)

    def mostrar_mas_vendidos(self):
        productos_ordenados = sorted(self.productos, key=lambda x: x[3], reverse=True)
        self.mostrar_productos(productos_ordenados)

    def mostrar_menos_vendidos(self):
        productos_ordenados = sorted(self.productos, key=lambda x: x[3])
        self.mostrar_productos(productos_ordenados)

    def iniciar_informe(self):
        self.root.mainloop()

