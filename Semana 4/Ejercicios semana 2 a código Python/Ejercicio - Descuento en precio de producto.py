"""Cree un programa que le pida un `precio de producto` al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
        1. Si el precio es menor a 100, el descuento es del 2%.
        2. Si el precio es mayor o igual a 100, el descuento es del 10%. """

precio_producto = int(input("Ingrese el precio del producto: "))

if (precio_producto < 100):
    descuento = precio_producto * 0.02
else:
    descuento = precio_producto * 0.1

precio_final = precio_producto - descuento

print(f'El precio total a pagar por su producto es de: {precio_final}, y recibió un descuento de: {descuento}')