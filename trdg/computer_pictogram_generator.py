import random as rnd

from PIL import Image, ImageColor, ImageFont, ImageDraw, ImageFilter
import numpy as np
import os

def generate(
    pictograms_path,
    pictograms,
    picto_size,
    space_width,
):
    total_width = len(pictograms) * picto_size + (len(pictograms) - 1) * space_width
    pictograms_img = Image.new("RGBA", (total_width, picto_size), (0, 0, 0, 0))
    pictograms_mask = Image.new("RGB", (total_width, picto_size), (0, 0, 0))


    for i, p in enumerate(pictograms):
        picto_image = Image.open(os.path.join(pictograms_path, p)).convert("RGBA")
        picto_image = picto_image.resize((picto_size, picto_size))
        pictograms_img.paste(picto_image, ((picto_size + space_width) * i, 0), picto_image)
        pictograms_mask.paste(picto_image, ((picto_size + space_width) * i, 0), picto_image.split()[3])
        pictograms_mask = pictograms_mask.point(lambda p: p > 0)
        pictograms_mask_array = np.asarray(pictograms_mask)
        pictograms_mask_array[:,:,0] = np.zeros([pictograms_mask_array.shape[0], pictograms_mask_array.shape[1]])
        pictograms_mask_array[:,:,1] = np.zeros([pictograms_mask_array.shape[0], pictograms_mask_array.shape[1]])
        pictograms_mask = Image.fromarray(pictograms_mask_array)

    return pictograms_img, pictograms_mask


