import sys
import os
from PIL import Image, ImageDraw,ImageColor
from itertools import product

filename_to_analyze = str(sys.argv[1])
tile_resolution = int(sys.argv[2])

dirname = filename_to_analyze.split(".")[0] + "_puzzle"
os.mkdir("./"+dirname)

def tile(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = list(product(range(0, h-h%d, d), range(0, w-w%d, d)))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{int(i/d)}_{int(j/d)}{ext}')
        img.crop(box).save(out)
        # i is vertical column count
        # j is horizontal row count
        row = int(j/d)
        column = int(j/d)
        
print("Done, go check in folder named "+dirname)
tile(filename_to_analyze,"./",dirname,tile_resolution)
