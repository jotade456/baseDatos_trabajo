import tkinter as Ventana
from tkinter import messagebox

class Vista_json:
    def __init__(self,controlador):
        self.ventana = Ventana.Tk()
        self.ventana.title("Crear Archivo")
        self.ventana.geometry("380x250")
        self.ventana.configure(bg="purple")
        self.objControlador=controlador

        self.label_style = {"bg": "lightblue"}
        self.entry_style = {"font": "Helvetica"}

        self.label_nombre = Ventana.Label(self.ventana, text="Nombre del archivo:", **self.label_style)
        self.label_nombre.grid(row=1, column=0, pady=10, padx=10)

        self.entry_nombre = Ventana.Entry(self.ventana, **self.entry_style)
        self.entry_nombre.grid(row=1, column=1, pady=10, padx=10)

        self.boton_crear = Ventana.Button(self.ventana, text="Crear", command=self.agregar_dato)
        self.boton_crear.grid(row=2, column=0, columnspan=2, pady=20, padx=10)

    def agregar_dato(self):
        nombre_archivo = self.entry_nombre.get()
        if nombre_archivo:
            self.entry_nombre.delete(0, Ventana.END)
            self.objControlador.guardar_informe(nombre_archivo)
            messagebox.showinfo("Información", "Archivo creado con éxito!")
            
        else:
            messagebox.showwarning("Advertencia", "Ambos campos son obligatorios.")


    def abrirVista(self):
        self.ventana.mainloop()