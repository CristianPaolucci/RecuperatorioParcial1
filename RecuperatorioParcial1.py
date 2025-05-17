nombres_producto = []
cant_producto = []

opcion = ""



while opcion != "5":
    print ("1. Agregar producto")
    print ("2. Agregar productos agotados")
    print ("3. Actualizar stock")
    print ("4. Ver todos los productos")
    print ("5. Salir")

    opcion = input ("Seleccione una opcion de 1-5: ")

    if opcion == "1":
        nombre = input ("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        nombres_producto.append(nombre)
        cant_producto.append(cantidad)
        print ("Producto agregado correctamente")

    elif opcion == "2":
        agotados = False
        print ("Productos agotados")
        for i in range (len(cant_producto)):
            if cant_producto [i] == 0:
                print (" " + nombres_producto[1])
                agotados = True
        if not agotados:
            print ("No hay productos agotados")

    elif opcion == "3":
        producto = input ("Ingrese el nombre del producto")
        encontrado = False
        for i in range (len(nombres_producto)):
            if nombres_producto[i]== producto:
                nueva_cantidad = int(input("Ingrese nueva cantidad"))
                cant_producto[i] = nueva_cantidad
                print ("Stock actualizado")
                encontrado = True
                break
        if not encontrado:
            print ("Producto no encontrado")

    elif opcion == "4":
        print ("Listado de productos")
        if len(nombres_producto)== 0:
            print ("No hay productos")
        else:
            for i in range (len(nombres_producto)):
                print ("Son" , nombres_producto[i] + str(cant_producto[i]))

    elif opcion == "5":
        print ("Gracias por usar el sistema")
    else:
        print("Opcion invalida")



    
    
