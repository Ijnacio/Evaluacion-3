import mantenedor_de_categorias, reportes



while True:
    print("***************************")
    print("*       Mundo libro       *")
    print("***************************")    
    print("""
[1] - Mantenedor Categorias
[2] - Reportes
[3] - Salir            """)

    opcion= int(input("Ingrese opcion: "))

    if opcion == 1:
        mantenedor_de_categorias.menu_categorias()

    elif opcion == 2:
        reportes.reportes()

    elif opcion == 3:
        break