#! python3

import glob
from itertools import chain
import os 

for file in chain(glob.iglob("**.png"), glob.iglob("**/*.png")):
    file_base = file[:-4]
    print(file)
    os.system(f'convert "{file}" -quality 90 "{file_base}.webp"')
    
