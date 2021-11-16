import os
from PIL import Image
import itertools

DIVIDER = "/"
BACKGROUND_PATH = "." + DIVIDER + "background.png"
CATEGORIES_PATH = "." + DIVIDER + 'categories' + DIVIDER
OUTPUT_PATH = "." + DIVIDER + 'output' + DIVIDER
FILEEXTENSION = "PNG"

def stackImages(image_list):
    variants = []
    background = Image.open(BACKGROUND_PATH)

    for img_path in image_list:
        img = Image.open(img_path)
        background.paste(img, (0, 0), img)
        variants.append(os.path.basename(img_path).split(".")[0])

    background.save(OUTPUT_PATH + "_".join(variants) + "." + FILEEXTENSION, FILEEXTENSION)

def main():
    combinations_folders = []
    categories_list = [name for name in os.listdir(CATEGORIES_PATH) if os.path.isdir(os.path.join(CATEGORIES_PATH, name))]

    for file_name in categories_list:
        path = CATEGORIES_PATH + file_name + DIVIDER
        files = [path + f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        combinations_folders.append(files)
    combinations_list = list(itertools.product(*combinations_folders))

    for item in combinations_list:
        stackImages(item)

if __name__ == '__main__':
    main()