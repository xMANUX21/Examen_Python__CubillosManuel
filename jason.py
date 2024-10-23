import json

def guardar(usuarios,bonos,totales):
    datos={
    "usuarios":usuarios,
    "bonos":bonos,
    "totales":totales
    }
    with open('datos.json','w') as archivo1:
        json.dump(datos,archivo1,indent=4)

def cargarDatos():
    try:
        with open('datos.json','r') as archivo1:
            datos=json.load(archivo1)
            usuarios=datos.get('usuarios',[])
            bonos=datos.get('bonos',[])
            totales=datos.get('totales',[])
            return usuarios,bonos,totales
        
    except FileNotFoundError:
        print("No se encontró el archivo de datos, se comenzará desde cero.")#En caso de que haya algun error , me va a retornar  listas vacias 
        return [], [], [], [], []
    except json.JSONDecodeError:
        print("Error al cargar los datos, archivo de datos corrupto.")
        return [], [], [], [], []









