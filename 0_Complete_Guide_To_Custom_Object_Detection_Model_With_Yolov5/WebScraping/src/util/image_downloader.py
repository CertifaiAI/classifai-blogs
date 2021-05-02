from PIL import Image
import requests
from io import BytesIO
import base64
import os

def save_image(src, counter, path):
    """Method for saving a single image"""

    cur_dir = os.getcwd()

    image_root_path = os.path.join(cur_dir, "images")
    if not os.path.isdir(image_root_path):
        os.mkdir(image_root_path)
    
    image_path = os.path.join(image_root_path, path)
    if not os.path.isdir(image_path):
        os.mkdir(image_path)

    output_path = os.path.join(image_path,f"{path}_{format(counter, '04d')}.png")

    if src.startswith("http"):
        try:
            response = requests.get(src, timeout=20)
            img = Image.open(BytesIO(response.content))
            img.save(output_path)
        except:
            return False
    else:
        try:
            img = Image.open(src)
            img.save(output_path)
        except:
            return False

    print(f"Save Image: {output_path}")
    return True


def save_images(src_list, path, img_num):
    """Method for saving a list of images"""
    
    counter = 1
    for src in src_list:
        if counter == img_num + 1:
            break
        if (save_image(src, counter, path)):
            counter += 1
        