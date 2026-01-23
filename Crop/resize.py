import os
from PIL import Image

def rescale_images(input_folder, output_folder, size=(224, 224)):
    # Crear la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterar sobre los archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
        # Comprobar si el archivo es una imagen válida
        if filename.lower().endswith(('.jpg')):
            try:
                input_path = os.path.join(input_folder, filename)  # Ruta completa del archivo de entrada
                output_path = os.path.join(output_folder, filename)  # Ruta completa del archivo de salida
                
                # Abrir y reescalar la imagen
                with Image.open(input_path) as img:
                    img_resized = img.resize(size)
                    img_resized.save(output_path)  # Guardar la imagen en la carpeta de salida
                    print(f"Imagen {filename} reescalada y guardada en {output_folder}.")
            except Exception as e:
                print(f"No se pudo procesar la imagen {filename}. Error: {e}")

# Configuración
input_folder = '.'  
output_folder = './copia_224' 

# Ejecutar la función
rescale_images(input_folder, output_folder)
