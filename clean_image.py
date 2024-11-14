import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from pathlib import Path
import PIL

input_dir = Path("./png")
output_dir = Path("./cleaned_jpg")

inputs = input_dir.glob("*")
for x in inputs:
    img = cv.imread(x, cv.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read, check with os.path.exists()"
    th = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,75,6)
    out_name = output_dir / (x.stem + ".jpg")
    print(out_name)
    cv.imwrite(out_name, th)




