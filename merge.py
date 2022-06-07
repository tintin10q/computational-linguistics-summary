#!/usr/bin/env python3

# Get all files from the export 

import json
import os
import re


def markdown_filenames() -> set:
    import glob
    found = list(glob.iglob('**.md'))
    found.sort()
    yield from found


if __name__ == '__main__':

    import sys

    if len(sys.argv) > 1:
        output = sys.argv[1]
    else:
        output = 'CL-Summary-Merged-Quinten'
    if not output.endswith('.md'):
        output += '.md'

    wcd = os.getcwd()

    # Clear output
    open(output, 'w+').close()

    with open(output, 'a+') as output_file:
        output_file.write(r"""
---
date: \today
fontsize: "11pt"
linestretch: 1.5
inks-as-notes: true
titlepage: true
titlepage-color: "C89343"
titlepage-text-color: "003267"
titlepage-rule-height: 4
logo: "images/logo.png"
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
subtitle: "Midterm"
author: "Quinten Cabo u789241 q.m.j.cabo@tilburguniversity.edu "
title: "Computational Linguistics Summary"
link-citations: true
---

This is the version with the images!

\pagebreak

""")
        with open('index.md', 'r+') as f:
            text = f.read()
            output_file.write(text)

    figure_finder = re.compile(r'!(\[.{0,}])\(\.\/images\/Pasted_image_[0-9]+\.png\)')
    header_finder = re.compile(r'# {0,}?[^#](.+)')
    global_image_count = 1
    visted = []
    for filename in markdown_filenames():

        if filename == 'index.md':
            continue
        if filename == output:
            continue
        text = ''
        path = os.path.join(wcd, filename)
        if not os.path.exists(path):
            print(f'skip {filename}')
            continue
        with open(path, 'r') as file:
            new_text = file.read() + '\n\n'
            new_text = new_text.replace('.webp', '.png')

            new_text = new_text.replace('../images/', './images/')
            new_text = new_text.replace('.././images', './images')
            new_text = new_text.replace('%20', '_')
            # new_text = new_text.replace('.../images', '../images')
            new_text = new_text.replace('(Pasted_', '(./images/Pasted_')
            # IT WAS THE IMAGE NAMES THEY CAN"T HAVE SPACES!!

            # If pasted replace with name of header.

            header = re.search(header_finder, new_text)
            if hasattr(header, 'group'):
                header = header.group()
            else:
                header = 'No Title'
            header = header[2:]  # Big hack but I don't care

            img_index = 1
            for found in re.finditer(figure_finder, new_text):
                for found in found.groups():
                    # Don't forget to put [] back
                    new_text = new_text.replace(found, f'[{header} {img_index}]')
                    img_index += 1

        with open(output, 'a+') as outputfile:
            outputfile.write(new_text)
    print()
    print(f'Now run:\npandoceisvogel {output}')
