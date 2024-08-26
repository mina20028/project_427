import os
from zipfile import ZipFile

def compress_each_image_separately(image_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(image_folder, filename)
            zip_filename = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.zip")
            with ZipFile(zip_filename, 'w') as zipf:
                zipf.write(file_path, os.path.basename(file_path))

image_folder = "E:\\Pictures 1-1000\\Images"
output_folder = "C:\\Users\\dell\\Desktop\\Zipfile\\ZipFile"

compress_each_image_separately(image_folder,output_folder)