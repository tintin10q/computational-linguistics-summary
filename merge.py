#!/usr/bin/env python3
# coding=utf-8

""" Use this Python script to generate one pdf out of all the notes.

The first command line argument will be the filename of the generated pdf
"""

from __future__ import annotations

import json
import os
from collections.abc import Generator
import glob
from itertools import chain

import shutil

import re


def find_filenames(extensions: [], excluded: list[str] = None, exclude_regex: str | re.Pattern = r'(?!)') -> Generator[str]:
	"""
		:param extensions: File exstensions to find. Should NOT include the . example: ['png', 'webp']
		:param excluded: List of filenames to exclude
		:param exclude_regex: Exclude files which match the regex. By default, is (?!) which matches nothing.
		:return: A generator which generates all the .png and .webp files

		Get image file names
	"""
	
	if excluded is None:
		excluded = []
	
	globs = [chain(glob.iglob(f'*.{extension}'),
	               glob.iglob(f'*/**.{extension}'),
	               glob.iglob(f'*/*/**.{extension}')
	               ) for extension in extensions]
	found = chain(*globs)
	
	if excluded or exclude_regex != '(?!)':  # Only apply filter if we actually have something to filter
		exclude_pattern = exclude_regex if isinstance(exclude_regex, re.Pattern) else re.compile(exclude_regex)
		
		def file_filter(f: str) -> bool:
			return f not in excluded and not re.search(exclude_pattern, f)
		
		yield from filter(file_filter, found)
	else:
		yield from found


# These markdown files will not be included in the export.

default_excluded_markdown = [
	'Classification.md',
	'Data.md',
	'Languages.md',
	'Prediction.md',
	'index.md',
	'Semantic-Similarity.md'
]

default_excluded_images = []

default_excluded_markdown.sort()  # Sort to make in faster
default_excluded_images.sort()

introduction_file = 'README.md'

default_excluded_markdown.append(introduction_file)

# basename with extension
# basename = os.path.basename(path)

output_header = r"""---
date: \today
fontsize: "11pt"
linestretch: 1.5
inks-as-notes: true
titlepage: true
titlepage-color: "C89343"
titlepage-text-color: "003267"
titlepage-rule-height: 4
logo: "logo.png"
logo-width: 100
page-background-opacity: 5
links-as-notes: false
lot: true
lof: true
listings-disable-line-numbers: true
listings-no-page-break: false
disable-header-and-footer: false
subparagraph: true
lang: "en-UK"
subtitle: "Midterm & Final"
author: "Quinten Cabo - quintencabo@gmail.com"
title: "Computational Linguistics Summary"
link-citations: true
variables:
	header-includes: |
    	\usepackage[Latin]{ucharclasses}
    	\newfontfamily\fallbackfont{Gentium Plus} % Or whatever font you prefer.
    	\setTransitionsFor{LatinExtendedAdditional}{\fallbackfont}{\normalfont}
---

Computational Linguistics

\pagebreak

"""

if __name__ == '__main__':
	
	""" To create the export we are going to:
0. Create tmp directory
1. Copy all images to the tmp directory
2. Create output file in tmp directory
3. Load each markdown file into memory one by one
3a. Change all the image links in the markdown files to the current directory
3b  Write the markdown file into one file
4. Renamed Pasted images to heading of file
5. Try to generate a .tex file from the markdown with pandoc
6. Try to Generate the pdf from the .tex with pandoc
6b. Copy the pdf and tex out of the tmp directory
7. Delete the tmp dir
"""
	
	import sys
	
	if len(sys.argv) > 1:
		output = sys.argv[1]
	else:
		output = 'CL-Summary-Merged-Quinten'
	output_md = output if output.endswith('.md') else output + '.md'
	
	default_excluded_markdown.append(output_md)
	
	tempdir_name = 'EXPORT'
	
	default_excluded_markdown.append(str(os.path.join(tempdir_name, output_md)))
	
	wcd = os.getcwd()
	tmp = os.path.join(wcd, tempdir_name)
	
	output_in_tmp = os.path.join(tmp, output_md)
	
	""" Step 0 """
	print(f'\033[92mCreating temporary dir:\033[0m {tempdir_name}')
	try:
		os.mkdir(tmp)
	except FileExistsError:
		if os.listdir(tmp):  # if not os.listdir('/home/varun/temp')
			# delete and recreate it, so we are sure its empty
			shutil.rmtree(tmp)
			os.mkdir(tmp)
	
	""" Step 1 """
	print('\033[92mMoving images:\033[0m')
	
	for image_file in find_filenames(['webp', 'png'], default_excluded_images, fr'^{tempdir_name}'):
		basename = os.path.basename(image_file)
		basename = basename.replace(' ', '_')  # image names can not have spaces
		print(f'Moved {basename}')
		destination = os.path.join(tmp, basename)
		shutil.copyfile(image_file, destination)
	
	""" Step 2 """
	print(f"\033[92mCreating export markdown file\033[0m: {output_in_tmp}")
	
	with open(output_in_tmp, 'w+') as output_file:
		output_file.write(output_header)
		with open(introduction_file, 'r') as introduction_file:
			output_file.write(introduction_file.read())
			output_file.write('\n\n')
	
	""" Step 3 """
	print("\033[92mProcessing markdown files:\033[0m")
	
	image_with_spaces_pattern = re.compile(r'(!\[.+]\([.\\/A-z0-9]+)(%20)([A-z 0-9.%]+\))')
	figure_finder = re.compile(r'!(\[.{0,}])\(\.\/Pasted_image_[0-9]+\.png\)')
	header_finder = re.compile(r'^# {0,}?[^#](.+)')
	
	# Go through all the markdown files
	for filename in find_filenames(['md'], default_excluded_markdown):
		with open(filename, 'r', encoding='utf-8') as file:
			text = file.read()
			
			while re.search(image_with_spaces_pattern, text):
				text = re.sub(image_with_spaces_pattern, r'\1_\3', text)
			
			# text = text.replace('.webp', '.png')
			
			text = text.replace(r'.../images', r'../images')
			text = text.replace(r'../images/', r'')
			text = text.replace(r'.././images', r'')
			text = text.replace(r'images/', r'')
			
			header = re.search(header_finder, text)
			
			if hasattr(header, 'group'):
				header = header.group()
			else:
				header = 'No Title'
			header = header[2:]  # Big hack but I don't care
			
			img_index = 1
			for found in re.finditer(figure_finder, text):
				for found in found.groups():
					# Don't forget to put [] back
					text = text.replace(found, f'[{header} {img_index}]')
					img_index += 1
		
		with open(output_in_tmp, 'a+', encoding='utf-8') as outputfile:
			outputfile.write(text)
			outputfile.write("\n\n")  # Add new lines between every file
		print('Processed:', filename)
	# We now have to go to the export dir to build
	os.chdir(tempdir_name)
	
	print(output_in_tmp)
	
	print('\033[92mAttempting to run pandoc to generate .tex file\033[0m')
	tex_output = os.path.join(tmp, output + '.tex')
	os.system(f'pandoc -s "{output_in_tmp}" -o "{tex_output}"')
	
	print('\033[92mAttempting to run pandoc to generate .pdf file\033[0m')
	pdf_output = os.path.join(tmp, output + '.pdf')
	r = os.system(f'pandoc -s "{output_in_tmp}" --pdf-engine=xelatex -o "{pdf_output}"')
	print('Exit code of pandoc pdf', r)
	
	if r == 0:
		print(f'It seems like pandoc had success. You have a pdf now at {pdf_output}')
		destination = os.path.join('..', pdf_output)
	
	print('\033[92mAttempting to run pandoc to generate fancy (eisvogel) .pdf file\033[0m')
	pdf_output_eisvogel = os.path.join(tmp, output + '-eisvogel' + '.pdf')
	r = os.system(f'pandoc {output_md} -o {pdf_output_eisvogel} --columns=50 --citeproc  --number-sections --pdf-engine xelatex --toc --dpi=300 --template=eisvogel --strip-comments')
	print('Exit code of pandoc with eisvogel is ', r)
	if r == 0:
		print(f'It seems like pandoc had success. You have a pdf now in {pdf_output_eisvogel}')

# If it doesn't find images you probably did not put anything in ![here]()
