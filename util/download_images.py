"""
This script downloads and processes images based on the specified parameters.

Functions:
- resize_image: Resizes the input image to a specified size.
- add_padding: Adds padding to the input image.
"""

import numpy as np
from pathlib import Path
from PIL import Image

workspace_path = Path.cwd()

# Change the path to the images you want to download
data = np.load(workspace_path / "generations" / "custom_modelV4.npy")

# Specify specific images to download (0 index), leave empty to download all images
images_to_download = [89, 141, 149, 234, 317, 366, 665]

# Change the path to the folder where you want to save the images
save_path = workspace_path / "images"
OUTPUT_SIZE = 462 # square image
PADDING = 50 # Padding width

def resize_image(image, h, w, original = 16):
    tiles_per_row = w // original
    tiles_per_col = h // original

    # Tiling the image
    image_512x512 = np.repeat(np.repeat(image, tiles_per_col, axis=0), tiles_per_row, axis=1)
    return image_512x512

def add_padding(image, padding_width = 10, color = 255):
    padded_image = np.pad(image, 
                        pad_width=((padding_width, padding_width), 
                                    (padding_width, padding_width), 
                                    (0, 0)), 
                        mode='constant', 
                        constant_values=color)
    return padded_image

if __name__ == "__main__":
    for i, img in enumerate(data):
        if not images_to_download or (i) in images_to_download:
            if img.dtype != np.uint8:
                img = (img * 255).astype(np.uint8)

            img = resize_image(img, OUTPUT_SIZE, OUTPUT_SIZE)
            img = add_padding(img, padding_width=PADDING)
            
            image = Image.fromarray(img)
            image.save(save_path / f'image{i}.png')
