import json
from datetime import datetime

archivo = "tareas.json"
tareas = []

# --- CARGA INICIAL (Persistencia) ---
# Intentamos leer el archivo al arrancar el programa
try:
    with open(archivo, "r") as f:
        # json.load convierte el texto del archivo en una lista de Python
        tareas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    # Si el archivo no existe o está vacío, mantenemos la lista vacía
    tareas = []

def agregarTarea(descripcion):
    print("Agregar Tarea")
    nueva_tarea = {}  
    # Determinamos el ID basado en la lista cargada
    if not tareas:
        nuevo_id = 1
    else:
        # Accedemos al ID del último elemento de la lista y sumamos 1
        nuevo_id = tareas[-1]["Id"] + 1

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    nueva_tarea["Id"] = nuevo_id
    nueva_tarea["Descripcion"] = descripcion
    nueva_tarea["Estatus"] = "ToDo"
    nueva_tarea["createdAt"] = ahora
    nueva_tarea["updatedAt"] = ahora
    
    # Agregamos el nuevo diccionario a nuestra lista en memoria RAM
    tareas.append(nueva_tarea)

    # --- GUARDADO AUTOMÁTICO (Persistencia) ---
    # Usamos 'w' para sobreescribir el archivo con la lista actualizada
    with open(archivo, "w") as f:
        # json.dump toma la lista y la escribe en formato JSON
        # indent=4 hace que el archivo sea legible para humanos
        json.dump(tareas, f, indent=4)
    
    print("Tarea guardada exitosamente.")


def mostrarTareas(filtro = None):
    print(f"-- Lista de Tareas ({filtro if filtro else 'Todas'}) ---")

    if not tareas:
        print("No hay tareas en la lista")
    else:

        hayTareas = False
        for tarea in tareas:
            if filtro is None or tarea["Estatus"] == filtro:
                print(f"[{tarea['Id']}] {tarea['Descripcion']} | {tarea['Estatus']} | Creada: {tarea['createdAt']} | Actualizada: {tarea['updatedAt']}")
                hayTareas = True
        if not hayTareas:
            print("No se encontraron tareas con ese criterio.")
        

def eliminarTareas():
    continuar = True

    print("Eliminar tareas")
    
    while continuar:
        mostrarTareas()

        if not tareas:
            break

        decision = int(input("Selecciona el indice de la tarea que quieras eliminar: "))

        encontrada = False

        for tarea in tareas:
            if tarea["Id"] == decision:
                tareas.remove(tarea)
                with open(archivo, "w") as f:
                    # json.dump toma la lista y la escribe en formato JSON
                    # indent=4 hace que el archivo sea legible para humanos
                    json.dump(tareas, f, indent=4)
                    print("Tarea Eliminada correctamente")
                    encontrada = True
                    break

        if not encontrada:
            print("El Id no está en la lista, vuelve a intentarlo")

        opcion = input("Deseas eliminar otra tarea: (s/n) ").lower()
        if opcion == "n":
            continuar = False


def actualizarTarea():

    continuar = True

    print("Actualizar Tarea")
    while continuar:
        mostrarTareas()
        if not tareas:
            break

        decision = int(input("Selecciona el indice de la tarea que quieras actualizar: "))

        encontrada = False

        for tarea in tareas:
            if tarea["Id"] == decision:
                encontrada = True
                print(f"Tarea seleccionada: {tarea['Descripcion']}")
                print("1. Cambiar Descripción")
                print("2. Cambiar Estatus")
                
                sub_opcion = input("¿Qué deseas modificar? ")
                
                if sub_opcion == "1":
                    nueva_desc = input("Nueva descripción: ")
                    tarea["Descripcion"] = nueva_desc
                    tarea["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                elif sub_opcion == "2":
                    nuevo_estatus = input("Nuevo estatus (1. ToDo/2. Done/3. En proceso): ")
                    if nuevo_estatus == "1":
                        tarea["Estatus"] = "ToDo"
                        tarea["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    elif nuevo_estatus == "2":
                        tarea["Estatus"] = "Done"
                        tarea["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    elif nuevo_estatus == "3":
                        tarea["Estatus"] = "En Proceso"
                        tarea["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        print("Opción no valida")
                
                # Guardamos los cambios en el JSON
                with open(archivo, "w") as f:
                    json.dump(tareas, f, indent=4)
                
                print("Tarea actualizada correctamente")
                break
        
        if not encontrada:
            print("El Id no está en la lista de Tareas")

        opcion = input("Deseas actualizar otra tarea: (s/n) ").lower()
        if opcion == "n":
            continuar = False


    



# --- MENÚ PRINCIPAL ---
print("*"*40)
print("Bienvenido a tu Gestor de Tareas")
print("*"*40)

continuar = True

while continuar:
    print("\n1. Agregar Tarea.")
    print("2. Mostrar Lista de tareas")
    print("3. Actualizar Tarea")
    print("4. Eliminar Tarea")
    print("5. Salir")

    opcion = input("¿Qué deseas hacer? ")

    match opcion:
        case "1":
            descripcion = input("Añade una descripción: ")
            agregarTarea(descripcion)
        case "2":
            print("1. Ver todas")
            print("2. Ver hechas (Done)")
            print("3. Ver en curso (En Proceso)")
            print("4. Ver pendientes (ToDo)")
            ver_opcion = input("Selecciona una opción: ")
            
            if ver_opcion == "1": mostrarTareas()
            elif ver_opcion == "2": mostrarTareas("Done")
            elif ver_opcion == "3": mostrarTareas("En Proceso")
            elif ver_opcion == "4": mostrarTareas("ToDo")
        case "3":
            actualizarTarea()
        case "4":
            eliminarTareas()
        case "5":
            print("Vuelve pronto!")
            continuar = False            
        case _:
            print("Opción no válida, vuelve a intentarlo")