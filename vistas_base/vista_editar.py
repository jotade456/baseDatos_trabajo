import tkinter as tk
from tkinter import messagebox

class edicion:
    def __init__(self, controlador):
        self.controlador = controlador
        self.editar_ventana = tk.Tk()
        self.editar_ventana.title("Edición de Producto - NexusPlay Studio")
        self.editar_ventana.geometry("450x450")
        self.editar_ventana.configure(bg="#e0e0e0")

        fuente = ("Arial", 12)
        self.categoria = tk.StringVar()

        contenedor_principal = tk.Frame(self.editar_ventana, bg="#ffffff", padx=20, pady=20, relief="raised", bd=2)
        contenedor_principal.place(relx=0.5, rely=0.5, anchor="center")

        self.entry_id = tk.Entry(contenedor_principal, font=fuente, highlightbackground="#b0c4de", highlightthickness=1)
        self.entry_nombre = tk.Entry(contenedor_principal, font=fuente, highlightbackground="#b0c4de", highlightthickness=1)
        self.entry_stock = tk.Entry(contenedor_principal, font=fuente, highlightbackground="#b0c4de", highlightthickness=1)
        self.entry_cantidad_vendida = tk.Entry(contenedor_principal, font=fuente, highlightbackground="#b0c4de", highlightthickness=1)

        self.crear_widgets(contenedor_principal, fuente)

    def crear_widgets(self, contenedor_principal, fuente):
        estilo_label = {"bg": "#ffffff", "font": fuente, "fg": "#333333"}
        estilo_boton = {"font": fuente, "bg": "#4682b4", "fg": "white", "activebackground": "#5b9bd5", "bd": 0}

        tk.Label(contenedor_principal, text="ID del Producto:", **estilo_label).grid(row=0, column=0, sticky="w", pady=5)
        self.entry_id.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Nombre del Producto:", **estilo_label).grid(row=1, column=0, sticky="w", pady=5)
        self.entry_nombre.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Stock del Producto:", **estilo_label).grid(row=2, column=0, sticky="w", pady=5)
        self.entry_stock.grid(row=2, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Cantidad Vendida:", **estilo_label).grid(row=3, column=0, sticky="w", pady=5)
        self.entry_cantidad_vendida.grid(row=3, column=1, pady=5, padx=10, sticky="ew")

        tk.Label(contenedor_principal, text="Categoría del Producto:", **estilo_label).grid(row=4, column=0, sticky="w", pady=5)

        tk.Button(contenedor_principal, text="Acción", command=lambda: self.seleccionar_categoria("Accion"), **estilo_boton).grid(row=4, column=1, pady=5, sticky="ew")
        tk.Button(contenedor_principal, text="Aventura", command=lambda: self.seleccionar_categoria("Aventura"), **estilo_boton).grid(row=5, column=1, pady=5, sticky="ew")
        tk.Button(contenedor_principal, text="Deportes", command=lambda: self.seleccionar_categoria("Deportes"), **estilo_boton).grid(row=6, column=1, pady=5, sticky="ew")
        tk.Button(contenedor_principal, text="Guardar Cambios", command=self.guardar_cambios, font=("Arial", 12, "bold"), bg="#ff4500", fg="white", bd=0, activebackground="#ff6347").grid(row=7, column=0, columnspan=2, pady=15, sticky="ew")

    def seleccionar_categoria(self, categoria):
        self.categoria.set(categoria)
        messagebox.showinfo("Categoría Seleccionada", f"Has seleccionado la categoría: {categoria}")

    def guardar_cambios(self):
        ID = self.entry_id.get()
        nombre = self.entry_nombre.get()
        cantidad = self.entry_stock.get()
        ventas = self.entry_cantidad_vendida.get()
        categoria = self.categoria.get()

        if ID and nombre and cantidad and ventas and categoria:
            try:
                self.controlador.editar_productos(ID, nombre, cantidad, ventas, categoria)
                messagebox.showinfo("Edición Exitosa", "Producto editado correctamente.")
                self.editar_ventana.destroy()
            except TypeError as e:
                messagebox.showerror("Error", f"Error al editar el producto: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    def iniciar_programa(self):
        self.editar_ventana.mainloop()

