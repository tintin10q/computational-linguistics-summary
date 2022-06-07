#! python3
# coding=utf-8

import glob
from itertools import chain
import os

if input('Do you have the convert command (imagemagick) command installed? Enter yes to continue:') != 'yes':
    print('You did not enter yes exiting...')
    exit()

for file in chain(glob.iglob("**.png"), glob.iglob("**/*.png")):
    file_base = file[:-4]
    print(file)
    os.system(f'convert "{file}" -quality 90 "{file_base}.webp"')
