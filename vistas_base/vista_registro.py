import tkinter as tk
from tkinter import messagebox

class abrir_registro_producto:
    def __init__(self, controlador):
        self.controlador = controlador
        self.registro_ventana = tk.Tk()
        self.registro_ventana.title("Registro de Producto NexusPlay Studio")
        self.registro_ventana.geometry("400x400")
        self.registro_ventana.configure(bg="#f5f5f5")

        fuente = ("Arial", 12)
        self.categoria = tk.StringVar()

        contenedor_principal = tk.Frame(self.registro_ventana, bg="#ffcccb", padx=20, pady=20)
        contenedor_principal.pack(fill="both", expand=True)

        self.entry_id = tk.Entry(contenedor_principal, font=fuente)
        self.entry_nombre = tk.Entry(contenedor_principal, font=fuente)
        self.entry_stock = tk.Entry(contenedor_principal, font=fuente)
        self.entry_cantidad_vendida = tk.Entry(contenedor_principal, font=fuente)

        self.crear_widgets(contenedor_principal, fuente)

    def crear_widgets(self, contenedor_principal, fuente):
        tk.Label(contenedor_principal, text="ID del Producto:", bg="#ffcccb", font=fuente).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_id.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Nombre del Producto:", bg="#ffcccb", font=fuente).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_nombre.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Stock del Producto:", bg="#ffcccb", font=fuente).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_stock.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Cantidad Vendida:", bg="#ffcccb", font=fuente).grid(row=3, column=0, sticky="w", pady=5)
        self.entry_cantidad_vendida.grid(row=3, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Categoría del Producto:", bg="#ffcccb", font=fuente).grid(row=4, column=0, sticky="w", pady=5)

        tk.Button(contenedor_principal, text="Acción", command=lambda: self.seleccionar_categoria("Accion"), font=fuente, bg="#ffcccb").grid(row=4, column=1, pady=5, sticky="ew")
        tk.Button(contenedor_principal, text="Aventura", command=lambda: self.seleccionar_categoria("Aventura"), font=fuente, bg="#ffcccb").grid(row=5, column=1, pady=5, sticky="ew")
        tk.Button(contenedor_principal, text="Deportes", command=lambda: self.seleccionar_categoria("Deportes"), font=fuente, bg="#ffcccb").grid(row=6, column=1, pady=5, sticky="ew")

        tk.Button(contenedor_principal, text="Guardar Producto", command=self.guardar_producto, font=fuente, bg="#ff6347", fg="white").grid(row=7, column=0, columnspan=2, pady=10, sticky="ew")

    def seleccionar_categoria(self, categoria):
        self.categoria.set(categoria)
        messagebox.showinfo("Categoría Seleccionada", f"Has seleccionado la categoría: {categoria}")

    def guardar_producto(self):
        ID = self.entry_id.get()
        nombre = self.entry_nombre.get()
        cantidad = self.entry_stock.get()
        ventas = self.entry_cantidad_vendida.get()
        categoria = self.categoria.get()

        if ID and nombre and cantidad and ventas and categoria:
            try:
                self.controlador.agregar_producto(ID, nombre, cantidad, ventas, categoria)
                messagebox.showinfo("Registro Exitoso", "Producto registrado correctamente.")
                self.registro_ventana.destroy()
            except TypeError as e:
                messagebox.showerror("Error", f"Error al registrar el producto: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    def iniciar_programa(self):
        self.registro_ventana.mainloop()



