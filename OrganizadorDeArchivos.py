import os
import shutil

# Define la ruta donde se encuentran los archivos que deseas organizar
ruta_origen = r'C:\Users\nahat\Videos'

# Define el directorio donde deseas que se almacenen los archivos organizados
ruta_destino = r'C:\Users\nahat\Videos'

# Crea el directorio de destino si no existe
if not os.path.exists(ruta_destino):
    os.makedirs(ruta_destino)

# Recorre todos los archivos en la ruta de origen
for archivo in os.listdir(ruta_origen):
    # Obtén la ruta completa del archivo
    ruta_completa = os.path.join(ruta_origen, archivo)
    # Si es un archivo (y no una carpeta) y tiene una extensión
    if os.path.isfile(ruta_completa) and '.' in archivo:
        # Obtiene la extensión del archivo
        extension = archivo.split('.')[-1]
        # Crea una carpeta con el nombre de la extensión, si no existe
        ruta_extension = os.path.join(ruta_destino, extension)
        if not os.path.exists(ruta_extension):
            os.makedirs(ruta_extension)
        # Mueve el archivo a la carpeta correspondiente
        destino_archivo = os.path.join(ruta_extension, archivo)
        
        # Maneja el caso en el que ya existe un archivo con el mismo nombre en la carpeta de destino
        contador = 1
        while os.path.exists(destino_archivo):
            nuevo_nombre = f"{archivo.split('.')[0]}_{contador}.{extension}"
            destino_archivo = os.path.join(ruta_extension, nuevo_nombre)
            contador += 1

        try:
            shutil.move(ruta_completa, destino_archivo)
            print(f"Archivo movido con éxito a: {destino_archivo}")
        except PermissionError as e:
            print(f"Error de permisos al mover el archivo: {e}")
