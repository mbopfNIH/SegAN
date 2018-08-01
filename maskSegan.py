from __future__ import print_function
import argparse
from PIL import Image, ImageDraw
import os
from ast import literal_eval
import matplotlib.pyplot as plt


############################################################################################
#
# maskSegan - Simple script that takes input and label images, a color mask and an output
#             filename, and masks the input image with a colored version of the mask. This
#             currently uses full opacity of the color - adding some transparency is top on
#             my list of enhancements.
#
# This script is designed to be run in a SegAN outputs directory. It doesn't accept command
# line parameters, yet, although the function is designed to do so. To run, simply cd into
# the outputs directory (e.g. outputs_2075) and run the following command ('$' is the prompt):
#       $ cd outputs_xxxx
#       $ python ../maskSegan.py
#
# 17 July 2018 - Mike Bopf
############################################################################################
def maskSegan(input, label, result, color, labelmaskfile, resultmaskfile, display):
    if not os.path.isfile(input):
        print("Error: Input file does not exist: ", input)
        return
    if not os.path.isfile(label):
        print("Error: Label file does not exist: ", label)
        return
    
    try:
        color = literal_eval(color)
        img = Image.new('RGB', (1000,1000), color)
#        img.show()
    except:
        print("Error: Invalid input color: ", color)
        return

    input_img = Image.open(input)
    mask = Image.open(label).convert("L")

    color_mask = Image.new('RGBA', input_img.size, color)
    
    color_mask.putalpha(mask)
    input_img.paste(color_mask, (0,0), color_mask)
    result_img = Image.open(result)

    # Write out the merged output file
    # NOTE: this overwrites the file!
    input_img.save(labelmaskfile)

    input_img = Image.open(input)
    mask = Image.open(result).convert("L")
    result_mask = Image.new('RGBA', input_img.size, color)
    result_mask.putalpha(mask)
    input_img.paste(result_mask, (0,0), result_mask)
    input_img.save(resultmaskfile)
    if display:
        result_mask.show()
        input_img.show()

# Use argparse to take in command line arguments
parser = argparse.ArgumentParser(description='Example')
parser.add_argument('--input', default='input_val.png', help='original input image')
parser.add_argument('--label', default='label_val.png', help='label mask image')
parser.add_argument('--result', default='result_val.png', help='label mask image')
parser.add_argument('--color', default='(0,0,255,200)', help='color of overlaid mask')
parser.add_argument('--labelmask', default='label_mask.png', help='masked label output file name')
parser.add_argument('--resultmask', default='result_mask.png', help='masked result output file name')
parser.add_argument('--display', default=False, help='Should masks attempt to be displayed')
opts = parser.parse_args()

maskSegan(opts.input, opts.label, opts.result, opts.color, opts.labelmask, opts.resultmask, opts.display)
