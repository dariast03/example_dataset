import os
from PIL import Image

# Directorio base de entrada y salida
input_base_dir = 'data/train'
output_base_dir = 'filter-data'

# Asegúrate de que el directorio de salida base existe
os.makedirs(output_base_dir, exist_ok=True)

# Función para verificar si un archivo es una imagen y convertirlo a JPG
def convert_to_jpg(file_path, output_path):
    try:
        with Image.open(file_path) as img:
            # Convertir a RGB si es necesario
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            # Guardar la imagen como JPG en el directorio de salida
            img.save(output_path, 'JPEG')
        return True
    except (IOError, ValueError) as e:
        print(f"Error al procesar {file_path}: {e}")
        return False

# Recorrer todos los subdirectorios de input_base_dir
for root, dirs, files in os.walk(input_base_dir):
    for file in files:
        file_path = os.path.join(root, file)
        relative_path = os.path.relpath(file_path, input_base_dir)
        output_dir = os.path.join(output_base_dir, os.path.dirname(relative_path))
        output_path = os.path.join(output_dir, os.path.splitext(file)[0] + '.jpg')

        # Asegúrate de que el directorio de salida existe
        os.makedirs(output_dir, exist_ok=True)

        # Verifica si el archivo es una imagen y conviértelo a JPG
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
            if convert_to_jpg(file_path, output_path):
                print(f"Convertido y movido: {file_path} a {output_path}")
            else:
                print(f"No se pudo convertir: {file_path}")

print("Proceso completado.")
