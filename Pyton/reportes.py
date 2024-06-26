import json
with open('biblioteca.json','r', encoding='utf-8') as file:
    leerJson = json.load(file)

with open('Reportes_biblioteca_mundo_libro.json','w', encoding='utf-8') as file:

    json.dump(leerJson['Prestamo'], file, ensure_ascii=False, indent=4 )


def reportes():
    contador = 0
    for i in leerJson["Prestamo"]:
       
        for j in leerJson["Libro"]:
            if i["LibroID"] == j["LibroID"]:
                contador +1
          
    print(contador)




