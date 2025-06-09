#1. Nombre del producto
while True: 
    Nombre = (input("Nombre del producto: "))

    if Nombre.isalpha():
        break
    else:
        print("Caracter no valido.")

#2. Precio unitario
while True:
    Precio = (input("Introduce el precio: "))

    if Precio.isdigit():
        Precio = float(Precio)
        break
    else: 
        print("Caracter no valido.")

#3. Cantidad de productos adquiridos
while True:
    NumProductos = (input("Cantidad de productos: "))

    if NumProductos.isdigit():
        NumProductos = int(NumProductos)
        break
    else: 
        print("Caracter no valido.")
    
#4. Porcentaje de descuento a aplicar
while True:
    Descuento = (input("El porcentaje de descuento es: "))

    if Descuento.isdigit():
        Descuento = int(Descuento)
        break
    else:
        print("Caracter no valido.")

#5. Determinar el precio sin descuento
print(f"Producto sin descuento: {Precio}$")

#6. Calcular el descuento especificado
Subtototal = Precio * NumProductos
DescuentoAplicado = Precio * (Descuento / 100)
Total = DescuentoAplicado

#7. Precio total de productos sin descuento
ProductosSinDescuento = Precio * NumProductos
print(f"Todos los productos sin descuento valen: {ProductosSinDescuento}$")

#8. Precio final
print(f"Tu producto con descuento es: {Total}$")