class Producto:
    def __init__(self):
        self.id = None
        self.nombre=None
        self.stock=None
        self.venta=None
        self.categoria=None
        self.productos=None

    def getId(self):
        return self.id

    def setId(self, datoId):
        self.id = datoId


    def getNombre(self):
        return self.nombre
    
    def setNombre(self, datonombre):
        self.nombre=datonombre


    def getStock(self):
        return self.stock
    
    def setStock(self, datostock):
        self.stock = datostock


    def getVenta(self):
        return self.venta
    
    def setVenta(self, datoventa):
        self.venta = datoventa


    def getCategoria(self):
        return self.categoria
    
    def setCategoria(self, datocategoria):
        self.categoria = datocategoria


    