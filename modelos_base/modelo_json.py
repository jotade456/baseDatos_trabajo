import json

class crear_archivo_informe():
    def __init__(self):
        self.texto=None
        
        
    def guardarDatos(self,dato_texto):
        self.texto=dato_texto
        return self.texto
    
    def crearArchivo(self,dato_texto,nombreArchivo):
        nombreArchivo=nombreArchivo+".txt"
        with open(nombreArchivo,"w") as archivoTexto:
            json.dump(dato_texto,archivoTexto)
            
            
    def deserializar(self, nombreArchivo):
        nombreArchivo=nombreArchivo+".txt"
        with open(nombreArchivo,"r")as archivoTexto:
            dato_texto=json.load(archivoTexto)
            return dato_texto