import os
import shutil

# Directorio origen
source_dir = 'data_by_departments'

# Directorio destino
dest_dir = 'data/train'

# Asegurarse de que el directorio de destino existe
os.makedirs(dest_dir, exist_ok=True)

# Iterar sobre cada subdirectorio en el directorio de origen
for department in os.listdir(source_dir):
    department_path = os.path.join(source_dir, department)

    if os.path.isdir(department_path):
        # Iterar sobre cada subdirectorio en el directorio del departamento
        for subfolder in os.listdir(department_path):
            subfolder_path = os.path.join(department_path, subfolder)

            if os.path.isdir(subfolder_path):
                # Imprimir cada subdirectorio
                print(f"Subfolder encontrado: {subfolder_path}")
                # Comentar la línea de copia
                dest_subfolder_path = os.path.join(dest_dir, subfolder)
                shutil.copytree(subfolder_path, dest_subfolder_path)
                # throw error


print("Todos los subfolders han sido listados.")
