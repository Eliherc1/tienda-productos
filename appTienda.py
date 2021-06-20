from clases.tienda import Tienda
from clases.producto import Producto

tienda1= Tienda("CYB STORE")

producto1=Producto("Huevos",100,"Lacteos y Huevos")
producto2=Producto("Arroz",700,"Abarrotes")
producto3=Producto("Papas",1000,"Verduras")
producto4=Producto("Leche",1000,"Lacteos y Huevos")

print(f"*******************BIENVENIDO A LA TIENDA {tienda1.mostrarTienda()}************")
tienda1.add_product(producto1).add_product(producto2).add_product(producto3).add_product(producto4)
tienda1.sell_product(0)
print("*********************LISTADO DE PRODUCTOS SIN INFLACION**************************")
print(tienda1.mostrarProd())

tienda1.inflation(0.02)
tienda1.set_clearance("Verduras",0.05)


print("*********************LISTADO DE PRODUCTOS CON INFLACION Y DESCUENTOS**************************")
print(tienda1.mostrarProd())

#huevos.print_info()