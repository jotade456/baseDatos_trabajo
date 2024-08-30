import tkinter as tk

class CatalogoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Catálogo de Productos")

        marco_superior = tk.Frame(root, bd=2, relief="groove")
        marco_superior.pack(fill="x")

        nombre_empresa = tk.Label(marco_superior, text="NexusPlay Studios", font=("Arial", 16))
        nombre_empresa.pack(side="left", padx=10, pady=10)

        logo = tk.Label(marco_superior, text="Logo", font=("Arial", 12), bg="gray", width=10, height=5)
        logo.pack(side="right", padx=10, pady=10)

        barra_nav = tk.Frame(root, bd=2, relief="groove")
        barra_nav.pack(fill="x")

        marco_categorias = tk.Frame(root, bd=2, relief="groove")
        marco_categorias.pack(fill="x")

        categorias = ["Registrar Compra", "Gestión de Productos", "Opiniones y Reseñas", "Soporte y Contacto"]
        for categoria in categorias:
            if categoria == "Registrar Compra":
                btn_categoria = tk.Button(marco_categorias, text=categoria)
            else:
                btn_categoria = tk.Button(marco_categorias, text=categoria)
            btn_categoria.pack(side="left", padx=10, pady=10)

        titulo_catalogo = tk.Label(root, text="Welcome to our catalog", font=("Arial", 14))
        titulo_catalogo.pack(pady=10)

        self.frame_catalogo = tk.Frame(root)
        self.frame_catalogo.pack(pady=10)

        for i in range(3):  
            for j in range(3):  
                producto_frame = tk.Frame(self.frame_catalogo, bg="#ffffff", bd=1, relief="solid")
                producto_frame.grid(row=i, column=j, padx=10, pady=10)

                img_label = tk.Label(producto_frame, text="Imagen", bg="gray", width=20, height=10)
                img_label.pack()

                info_label = tk.Label(producto_frame, text=f"Producto {i*3 + j + 1}\nCategoría: X\nPrecio: $Y", font=("Arial", 10))
                info_label.pack()

    def agregar_producto(self, producto):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = CatalogoApp(root)
    root.mainloop()