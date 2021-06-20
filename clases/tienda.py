class Tienda:
    def __init__(self,nombre):
        self.nombre= nombre
        self.listaProductos= []

    def add_product (self, new_product):
        #toma un producto y lo agrega a la tienda
        self.listaProductos.append(new_product)
        print (f"Producto agregado")
        return self

    def sell_product (self, id):
        #elimina el producto de la lista de productos de la tienda dada la identificación 
        # (suponga que id es el índice del producto en la lista) e imprima su información.
        self.listaProductos.pop(id)
        print(f"Producto Vendido")
        return self
    def inflation(self, percent_increase):
        #aumenta el precio de cada producto por el percent_increase dado 
        # (¡use el método que escribió en la clase Product!)
        for p in self.listaProductos:
            p.update_price(percent_increase, True)
        return self
    def set_clearance (self, category, percent_discount):
        #actualiza todos los productos que coinciden con la categoría dada reduciendo 
        # el precio en el percent_discount dado (¡use el método que escribió en la clase Product!)
        for p in self.listaProductos:
            if p.categoria == category:
                p.update_price(percent_discount,False)
    def mostrarProd(self):
        for p in self.listaProductos:
            p.print_info()
    def mostrarTienda(self):
        return self.nombre


