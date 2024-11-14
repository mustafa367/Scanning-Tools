import os 
import shutil

page_count = 1
for page in range(1, page_count + 1):
    i = (page - 1) * 3 + 2
    name = "./pbm/img-" + str(page).zfill(3) + "-" + str(i).zfill(3) + ".pbm"
    out  = "./pbm/pbm"
    shutil.move(name, out)