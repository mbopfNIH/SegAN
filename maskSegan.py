from __future__ import print_function
import argparse
from PIL import Image, ImageDraw
import os
from ast import literal_eval

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
def maskSegan(input='input.png', label='label.png', color=(0,0,255), output='maskedOut.png'):
    if not os.path.isfile(input):
        print("Error: Input file does not exist: ", input)
        return
    if not os.path.isfile(label):
        print("Error: Label file does not exist: ", label)
        return
    
    try:
        print(type(color))
        color = literal_eval(color)
        img = Image.new('RGB', (1000,1000), color)
#        img.show()
    except:
        print("Error: Invalid input color: ", color)
        return

    input_img = Image.open(input)
    input_img.show()
    mask = Image.open(label).convert("L")
    mask_color = Image.new('RGBA', input_img.size, color)
    
    mask_color.putalpha(mask)
    mask_color.show()
    input_img.paste(mask_color, (0,0), mask_color)
    input_img.show()

    # Write out the merged output file
    # NOTE: this overwrites the file!
    input_img.save(output)

# Use argparse to take in command line arguments
parser = argparse.ArgumentParser(description='Example')
parser.add_argument('-i', '--input', default='input.png', help='original input image')
parser.add_argument('-l', '--label', default='label.png', help='label mask image')
parser.add_argument('-c', '--color', default='(0,0,255)', help='color of overlaid mask')
parser.add_argument('-o', '--output', default='maskedOut.png', help='masked output file name')
opts = parser.parse_args()

maskSegan(opts.input, opts.label, opts.color, opts.output)
