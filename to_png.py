

import glob

from PIL import Image
from pathlib import Path


from_format = 'webp'

for image_file in glob.iglob(f'images/**.{from_format}'):
	im = Image.open(image_file)
	stem = Path(image_file).resolve().stem
	print(stem+'.png')
	im.save(stem +'.png', format="png", lossless=True)
