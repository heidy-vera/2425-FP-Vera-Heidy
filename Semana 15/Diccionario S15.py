# Crear un diccionario con los datos de una persona ficticia
Informacion_personal = {
    "nombre": "Juliana Ramirez",
    "edad": 28,
    "ciudad": "Cuenca",
    "profesion": "Arquitecta"
}

# Modificar la clave "ciudad"
Informacion_personal["ciudad"] = "Tena"

# Agregar una nueva clave que repesente la profesion ,"experiencia"
Informacion_personal["experiencia"] = "5 años en diseño y construcción"

# Agregar una nueva clave que represente "telefono"
if "telefono" not in Informacion_personal:
    Informacion_personal["telefono"] = "0987834212"

# Eliminar la clave "edad" del diccionario
Informacion_personal.pop("edad", None)

# Imprimir el diccionario final
print("Diccionario Final:", Informacion_personal)