import json

with open('biblioteca.json','r', encoding='utf-8') as file:
    leerJson = json.load(file)

def leer_categoria():
    for i in leerJson["Categoria"]:
        print (f"""
                CategoriaID : {i["CategoriaID"]} 
                Nombre      : {i["Nombre"]}                

              """)

def agregar_categoria(nombre):
    nueva_categoria = {
            "CategoriaID": {len("CategoriaID")+1} ,
            "Nombre" : nombre 

    }
    leerJson["Categoria"].append(nueva_categoria)


def editar_categoria():
   categoriaId = int(input("Ingrese Id para editar categoria"))
   nombre = input("Ingresa nombre para el producto")

   for categoria in leerJson["Categoria"]:
       if categoriaId == categoria["CategoriaID"]:
           categoria["Nombre"] = nombre

def buscar_categoria():
    
    categoriaId = int(input("Ingrese Id para buscar categoria: "))
    for categoria in leerJson["Categoria"]:
       if categoriaId == categoria["CategoriaID"]:
            print(categoria["Nombre"])    
       else: print("Id invalido, no existe categoria")    

def eliminar(id,nombre):

    for categoria in leerJson["Categoria"]:
        if id == categoria["CategoriaID"]:
            categoria["Categoria"].pop()
        
        elif nombre == categoria["Nombre"]:
            categoria["Nombre"].pop()
        





           
        
    


#pop, remove, del

def menu_categorias():
    while True:
        print("***************************")
        print("*  MANTENEDOR CATEGORIAS   *")
        print("***************************")    
        print("""
              [1] - agregar categoria
              [2] - Editar Categoria
              [3] - Eliminar Categoria
              [4] - Buscar Categoria
              [5] - Mostrar Categotiras :)
              [6] - Volver                 """)
        
        opcion = int(input("Ingresa Opcion: "))
        
        if opcion == 1: agregar_categoria()
        
  
        elif opcion == 2: editar_categoria()
            
        elif opcion == 3: eliminar()

        elif opcion == 4: buscar_categoria()

        elif opcion == 5: break

        break

