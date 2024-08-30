import tkinter as tk
from tkinter import messagebox

class abrir_registro_producto:
    def __init__(self):
        registro_ventana = tk.Tk()
        registro_ventana.title("Registro de Compra NexusPlay Studio")
        registro_ventana.geometry("400x400")
        registro_ventana.configure(bg="#f5f5f5")  

        fuente = ("Arial", 12)

    
        categoria = tk.StringVar(value="Acción")  

        contenedor_principal = tk.Frame(registro_ventana, bg="#ffcccb", padx=20, pady=20)
        contenedor_principal.pack(fill="both", expand=True)

        label_nombre = tk.Label(contenedor_principal, text="Nombre del Producto:", bg="#ffcccb", font=fuente)
        label_nombre.grid(row=0, column=0, sticky="w", pady=5)
        entry_nombre = tk.Entry(contenedor_principal, font=fuente)
        entry_nombre.grid(row=0, column=1, pady=5, padx=10, sticky="ew")

        label_precio = tk.Label(contenedor_principal, text="Precio del Producto ($):", bg="#ffcccb", font=fuente)
        label_precio.grid(row=1, column=0, sticky="w", pady=5)
        entry_precio = tk.Entry(contenedor_principal, font=fuente)
        entry_precio.grid(row=1, column=1, pady=5, padx=10, sticky="ew")

        label_categoria = tk.Label(contenedor_principal, text="Categoría del Producto:", bg="#ffcccb", font=fuente)
        label_categoria.grid(row=2, column=0, sticky="w", pady=5)

        contenedor_categoria = tk.Frame(contenedor_principal, bg="#ffcccb")
        contenedor_categoria.grid(row=2, column=1, pady=5, sticky="ew")
        
        categorias = ["Acción", "Aventura", "Deportes"]
        for cat in categorias:
            radio = tk.Radiobutton(contenedor_categoria, text=cat, variable=categoria, value=cat, bg="#ffcccb", font=fuente)
            radio.pack(anchor='w')

        label_stock = tk.Label(contenedor_principal, text="Stock del Producto:", bg="#ffcccb", font=fuente)
        label_stock.grid(row=3, column=0, sticky="w", pady=5)
        entry_stock = tk.Entry(contenedor_principal, font=fuente)
        entry_stock.grid(row=3, column=1, pady=5, padx=10, sticky="ew")

        def guardar_producto():
            nombre_producto = entry_nombre.get()
            precio_producto = entry_precio.get()
            categoria_producto = categoria.get()
            stock_producto = entry_stock.get()

            if nombre_producto and precio_producto and categoria_producto and stock_producto:
                producto = {
                    "Nombre": nombre_producto,
                    "Precio": precio_producto,
                    "Categoría": categoria_producto,
                    "Stock": stock_producto
                }
                callback_agregar_producto(producto)
                registro_ventana.destroy()
            else:
                messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        
        boton_guardar = tk.Button(contenedor_principal, text="Guardar Producto", command=guardar_producto, font=fuente, bg="#ff6347", fg="white")
        boton_guardar.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

        def visualizar_registro():
            pass
        
        boton_visualizar = tk.Button(contenedor_principal, text="Visualizar Registro", command=visualizar_registro, font=fuente, bg="#ff6347", fg="white")
        boton_visualizar.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

        registro_ventana.grid_columnconfigure(1, weight=1)

        registro_ventana.mainloop()


x=abrir_registro_producto()