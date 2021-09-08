#Crear un programa donde se permita la compra de productos.
#Al iniciar el mismo, se le solicitará al usuario que ingrese el código de producto a adquirir.
#En el sistema existirán 3 tipos de productos diferentes,por compra solo se podrá levar un tipo de producto.#
#Una vez ingresado el producto a llevar,el sistema deberá solicitar la cantidad a comprar.
#Se podra realizar la compra de un maximo de 3 productos.
#Si se compran 2 productos se aplicará un descuento del 50% en la segunda unidad.
#Si se compran 3 productos se abonarán 2.
#Finalmente, debe mostrar el total a pagar en funcion al precio del producto y el descuento aplicado

cod = 0
cant = 0
total = 0
totparcial= 0
precio_1= 1200
precio_2= 999
precio_3 = 300

#Obtengo el artículo
cod=int(input("Ingrese el código de articulo que desea llevar: "))

#Si el artículo no es válido
if cod>3 or cod<1:
    print(f"Ingrese un codigo de articulo valido") 
#Si el artículo es válido
else:
    #Obtengo la cantidad a llevar
    cant=int(input("Ingrese la cantidad a llevar: "))
    #Según la cantidad a llevar calculo el descuento
    if cant==1: 
        totparcial=1
    elif cant==2:
        totparcial=1.5
    elif cant==3:
        totparcial=2
    
    #Si la cantidad ingresada es mayor a 3
    if cant>3:
        print(f"La cantidad de articulos no puede ser mayor a 3 ")
    #Si la cantidad ingresada es menor a 1
    elif cant<1:
        print(f"La cantidad debe ser mayor a 0 ")
    #Si la cantidad ingresada es entre 1 y 3    
    else:
        #Calculo el total a pagar en función al descuento y al precio del artículo
        if cod==1:
            total=totparcial*precio_1
        elif cod==2:
            total=totparcial*precio_2
        elif cod==3:
            total=totparcial*precio_3
        #Muestro el total a pagar
        print(f"El total a pagar es de: {total}")