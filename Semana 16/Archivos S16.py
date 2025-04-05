#Crea un archivo llamado my_notes.txt.
#Abre el archivo
Archivo = open('my_notes.txt', 'w')

#Escribir tres lineas
Archivo.write('La semana de examenes se acerca y estoy nerviosa.\n')
Archivo.write('Espero no quedarme en ninguna materia.\n')
Archivo.write('Ya quiero que lleguen las vacaciones.\n')

#Cerrar el archivo
Archivo.close()

#Abrir el archivo para la lectura
Archivo = open('my_notes.txt','r')

#Mostrar en la consola las lineas leidas
print(Archivo.readline().strip())
print(Archivo.readline().strip())
print(Archivo.readline().strip())

#cerramos el archivo
Archivo.close()