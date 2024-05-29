import rembg
from PIL import Image

def remove_background(input_path, output_path):
    with open(input_path, "rb") as input_file, open(output_path, "wb") as output_file:
        input_data = input_file.read()
        output_data = rembg.remove(input_data)
        output_file.write(output_data)

# Specify input and output paths
input_image_path = r"C:\Users\Laboratorio a\PycharmProjects\image-downloader\dataset\cueca chapaca vestimenta\Image_3.jpg"

output_image_path = "output_image.png"

# Remove background
remove_background(input_image_path, output_image_path)

# Display the results
original_image = Image.open(input_image_path)
removed_background_image = Image.open(output_image_path)

original_image.show(title="Original Image")
removed_background_image.show(title="Image with Removed Background")