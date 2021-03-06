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
def maskSegan(input, label, result, lcolor, rcolor, labeloutfile, resultoutfile, blendoutfile, display, path, output):

    input = os.path.join(path, input)
    if not os.path.isfile(input):
        print("Error: Input file does not exist:", input)
        return
    label = os.path.join(path, label)
    if not os.path.isfile(label):
        print("Error: Label file does not exist:", label)
        return
    result = os.path.join(path, result)
    if not os.path.isfile(result):
        print("Error: Result file does not exist:", result)
        return

    try:
        lcolor = literal_eval(lcolor)
        img = Image.new('RGBA', (10,10), lcolor)
    except:
        print("Error: Invalid input color:", lcolor)
        return

    try:
        rcolor = literal_eval(rcolor)
        img = Image.new('RGBA', (10,10), rcolor)
    except:
        print("Error: Invalid input color:", rcolor)
        return

    label_img = Image.open(label)
    label_img = label_img.convert("L")
    data = label_img.getdata()
    ldata = []
    for pix in data:
        if pix == 0:
            ldata.append((0, 0, 0, 0))
        else:
            ldata.append(lcolor)
    lmask = Image.new("RGBA", label_img.size)
    lmask.putdata(ldata)

    result_img = Image.open(result)
    result_img = result_img.convert("L")
    data = result_img.getdata()
    rdata = []
    for pix in data:
        if pix == 0:
            rdata.append((0, 0, 0, 0))
        else:
            rdata.append(rcolor)
    rmask = Image.new("RGBA", result_img.size)
    rmask.putdata(rdata)

    # Blend the two masks equally
    blend = Image.blend(rmask, lmask, 0.5)

    # Open the original input image and paste the blended mask a top using the alpha
    # values of the provided masks.
    input_img = Image.open(input)
    input_img.paste(blend, (0,0), blend)

    # Write out the merged output file
    # NOTE: these overwrite the files!
    if output:
        lmask.save(os.path.join(path, labeloutfile))
        rmask.save(os.path.join(path, resultoutfile))
        input_img.save(os.path.join(path, blendoutfile))

    # Display the images if the "display" argument is set
    if display:
        lmask.show()
        rmask.show()
        input_img.show()

# Use argparse to take in command line arguments
parser = argparse.ArgumentParser(description='Example')
parser.add_argument('--input', default='input_val.png', help='original input image')
parser.add_argument('--label', default='label_val.png', help='label mask image')
parser.add_argument('--result', default='result_val.png', help='label mask image')
parser.add_argument('--lcolor', default='(0,0,255,128)', help='color of label mask')
parser.add_argument('--rcolor', default='(255,0,0,128)', help='color of result mask')
parser.add_argument('--labeloutfile', default='label_mask.png', help='masked label output file name')
parser.add_argument('--resultoutfile', default='result_mask.png', help='masked result output file name')
parser.add_argument('--blendoutfile', default='blend_mask.png', help='blended mask overlay output file name')
parser.add_argument('--display', default=True, help='Should masks attempt to be displayed')
parser.add_argument('--path', default='./', help='Directory path to prepend to all files')
parser.add_argument('--output', default='True', help='Should output files be written')
opts = parser.parse_args()

maskSegan(opts.input, opts.label, opts.result, opts.lcolor, opts.rcolor, opts.labeloutfile,
          opts.resultoutfile, opts.blendoutfile, opts.display, opts.path, opts.output)
