import tkinter as tk
from tkinter import messagebox

class Vista:
    def __init__(self, controlador):
        self.root = tk.Tk()
        self.root.title("Inicio de Sesión")
        self.root.geometry("350x350")
        self.root.configure(bg="lightgray")
        self.controlador = controlador

        self.nombre = tk.StringVar()
        self.contraseña = tk.StringVar()
        self.rol = tk.StringVar(value="Usuario")

        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self.root, text="Nombre de usuario:", bg="lightgray").pack(pady=5)
        tk.Entry(self.root, textvariable=self.nombre).pack(pady=5)

        tk.Label(self.root, text="Contraseña:", bg="lightgray").pack(pady=5)
        tk.Entry(self.root, textvariable=self.contraseña, show='*').pack(pady=5)

        tk.Label(self.root, text="Selecciona tu rol:", bg="lightgray").pack(pady=5)
        tk.Radiobutton(self.root, text="Administrador", variable=self.rol, value="Administrador", bg="lightgray").pack(anchor='w')
        tk.Radiobutton(self.root, text="Usuario", variable=self.rol, value="Usuario", bg="lightgray").pack(anchor='w')

        tk.Button(self.root, text="Iniciar sesión", command=self.boton_presionado).pack(pady=20)

    def boton_presionado(self):
        nombre_texto = self.nombre.get()
        contraseña_texto = self.contraseña.get()
        rol_texto = self.rol.get()

        if nombre_texto and contraseña_texto and rol_texto:
            if self.controlador.enviar_datos(nombre_texto, contraseña_texto, rol_texto):
                self.cerrar_ventana()
                self.controlador.verificar_usuario(rol_texto)
            else:
                messagebox.showerror("Error", "Usuario, contraseña o rol incorrectos.")
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa todos los datos.")

    def iniciar_vista(self):
        self.root.mainloop()

    def cerrar_ventana(self):
        self.root.withdraw()




