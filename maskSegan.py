from __future__ import print_function
from PIL import Image, ImageDraw
import os
import sys

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

    # Write out both the colorMask and the merged output file
    # NOTE: this overwrites the file!
    mask_color.save('colorMask.png')
    input_img.save(output)

maskSegan()
