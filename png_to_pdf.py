import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path
import PIL

input_dir = Path("./cleaned")
output_file = Path("./out.pdf")

inputs = input_dir.glob("*")
imgs = []
for x in inputs:
    img = PIL.Image.open(x)
    imgs.append(img)

imgs[0].save(output_file, save_all=True, append_images=imgs[1:])