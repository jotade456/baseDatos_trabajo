import tkinter as tk
from tkinter import messagebox

class AdministradorInformes:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Informes")
        self.root.geometry("400x200")

        self.label_titulo = tk.Label(root, text="Gestión de Informes", font=("Arial", 16))
        self.label_titulo.pack(pady=10)

        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(expand=True)

        self.btn_crear = tk.Button(self.frame_botones, text="Crear Informe", command=self.crear_informe)
        self.btn_crear.grid(row=0, column=0, padx=10, pady=10)

        self.btn_editar = tk.Button(self.frame_botones, text="Editar Informe", command=self.editar_informe)
        self.btn_editar.grid(row=0, column=1, padx=10, pady=10)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Informe", command=self.eliminar_informe)
        self.btn_eliminar.grid(row=0, column=2, padx=10, pady=10)

    def crear_informe(self):
        messagebox.showinfo("Éxito", "Informe creado con éxito.")

    def editar_informe(self):
        messagebox.showinfo("Éxito", "Informe editado con éxito.")

    def eliminar_informe(self):
        messagebox.showinfo("Éxito", "Informe eliminado con éxito.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AdministradorInformes(root)
    root.mainloop()
