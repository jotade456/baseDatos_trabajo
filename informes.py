import tkinter as tk
from tkinter import ttk, messagebox

class Informes:
        productos = []

        # Función para mostrar detalles del producto seleccionado
        def mostrar_detalles(event):
            item_seleccionado = tabla.selection()
            if item_seleccionado:
                producto = tabla.item(item_seleccionado)["values"]
                mensaje = f"Nombre: {producto[0]}\nPrecio: {producto[1]}\nCategoría: {producto[2]}\nStock: {producto[3]}"
                messagebox.showinfo("Detalles del Producto", mensaje)

        # Función para actualizar la tabla con los productos
        def actualizar_tabla():
            tabla.delete(*tabla.get_children())
            for producto in productos:
                tabla.insert("", tk.END, values=(producto["Nombre"], producto["Precio"], producto["Categoría"], producto["Stock"]))

        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("Informes de Productos - Tienda de Juegos")
        ventana.geometry("600x400")
        ventana.configure(bg="lightgrey")

        # Etiqueta de la interfaz
        label_titulo = tk.Label(ventana, text="Informes de Productos", font=("Arial", 16), bg="lightgrey")
        label_titulo.pack(pady=10)

        # Crear un contenedor para la tabla
        frame_tabla = tk.Frame(ventana)
        frame_tabla.pack(pady=10)

        # Crear la tabla
        tabla = ttk.Treeview(frame_tabla, columns=("Nombre", "Precio", "Categoría", "Stock"), show="headings")
        tabla.pack(side="left")

        # Definir encabezados de la tabla
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Precio", text="Precio")
        tabla.heading("Categoría", text="Categoría")
        tabla.heading("Stock", text="Stock")

        # Agregar un scrollbar a la tabla
        scrollbar = tk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        scrollbar.pack(side="right", fill="y")
        tabla.configure(yscroll=scrollbar.set)

        # Bind para mostrar los detalles del producto al hacer doble clic en un elemento
        tabla.bind("<Double-1>", mostrar_detalles)

        # Iniciar el bucle principal de la interfaz
        ventana.mainloop()


X=Informes()