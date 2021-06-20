class Producto:
    def __init__(self,nombreProd,precio,categoria):
        self.nombreProd = nombreProd
        self.precio = precio
        self.categoria = categoria

    def print_info (self):
        print (f"Nombre Producto: {self.nombreProd}, Precio: {self.precio}, Categoria: {self.categoria}")
    def update_price(self, percent_change, is_increased=True):
        #actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje 
        # de cambio proporcionado. Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
        if is_increased:
            self.precio = self.precio * (1+percent_change)
        else: 
            self.precio = self.precio * (1-percent_change)