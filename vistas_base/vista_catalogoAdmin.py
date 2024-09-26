import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk

class CatalogoApp:
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

        tk.Button(self.root, text="Guardar Informe", command=self.guardar_informe, font=("Arial", 12), bg="#4682b4", fg="white").pack(pady=10)
        
        tk.Button(self.root, text="Ver Informe", command=self.leer_deserializado, font=("Arial", 12), bg="#32cd32", fg="white").pack(pady=10)
        
        tk.Button(self.root, text="Editar producto", command=self.editar_producto, font=("Arial", 12), bg="#32cd32", fg="white").pack(pady=10)

        tk.Button(self.root, text="Borrar Registro", command=self.eliminar_producto, font=("Arial", 12), bg="#ff0000", fg="white").pack(pady=10)

        # Combobox para filtrar por categoría
        self.combo_categoria = ttk.Combobox(self.root, state="readonly")
        self.combo_categoria.pack(pady=10)
        self.cargar_categorias()

        tk.Button(self.root, text="Filtrar por Categoría", command=self.filtrar_por_categoria, font=("Arial", 12), bg="#ff6347", fg="white").pack(pady=10)
        
        titulo_catalogo = tk.Label(self.root, text="Catálogo de Productos", font=("Arial", 14))
        titulo_catalogo.pack(pady=10)

        self.frame_catalogo = tk.Frame(self.root)
        self.frame_catalogo.pack(pady=10)

    def cargar_categorias(self):
        categorias = self.controlador.modelo_catalogo.obtener_productos()  # Obtener productos
        categorias_unicas = set(producto[4] for producto in categorias)  # la categoría está en el índice 4
        self.combo_categoria['values'] = list(categorias_unicas)  # Establecer categorías únicas en el Combobox

    def crear_botones_acciones(self, marco_categorias):
        acciones = ["Registrar producto", "Ver informe productos"]
        for accion in acciones:
            btn_categoria = tk.Button(marco_categorias, text=accion, command=lambda c=accion: self.boton_accion(c))
            btn_categoria.pack(side="left", padx=10, pady=10)

    def boton_accion(self, accion):
        if accion == "Registrar producto":
            self.controlador.abrir_registro()
        elif accion == "Más Vendidos":
            pass
        elif accion == "Ver informe productos":
            self.controlador.abrir_vista_informe()

    def guardar_informe(self):
        self.controlador.abrir_vista_json()

    def filtrar_por_categoria(self):
        categoria = self.combo_categoria.get()  # Obtener categoría seleccionada
        if categoria:
            self.mostrar_productos(categoria)

    def mostrar_productos(self, categoria=None):
        for child in self.frame_catalogo.winfo_children():
            child.destroy()

        if categoria:
            productos = self.controlador.modelo_catalogo.obtener_productos_por_categoria(categoria)
        else:
            productos = self.controlador.modelo_catalogo.obtener_productos()
            
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

    def editar_producto(self):
        self.controlador.abrir_edicion()

    def eliminar_producto(self):
        id_producto = simpledialog.askinteger("Eliminar Producto", "Ingrese el ID del producto a eliminar:")
        if id_producto:
            confirmacion = messagebox.askyesno("Confirmar Eliminación", f"¿Está seguro de que desea eliminar el producto con ID {id_producto}?")
            if confirmacion:
                eliminado = self.controlador.eliminar_producto_por_id(id_producto)
                if eliminado:
                    messagebox.showinfo("Producto Eliminado", f"El producto con ID {id_producto} ha sido eliminado.")
                    self.actualizar_catalogo()
                else:
                    messagebox.showerror("Error", f"No se encontró el producto con ID {id_producto}.")

    def leer_deserializado(self):
        datoArchivo = simpledialog.askstring("Digitar", "Digite nombre del archivo")
        try:
            if datoArchivo:
                texto = self.controlador.deserializar(datoArchivo)
                messagebox.showinfo("Contenido del archivo", texto)
        except:
            messagebox.showerror("Error", "El nombre del archivo no es válido")

    def actualizar_periodicamente(self):
        self.actualizar_catalogo()
        self.root.after(9000, self.actualizar_periodicamente)

    def iniciar_catalogo(self):
        self.root.mainloop()

