#CUDA_VISIBLE_DEVICES=X python predict.py --statedict netstate.pth --cuda --inputfile test1.jpg --outdir ./predouts
from __future__ import print_function
import argparse
import os
from PIL import Image
import torch
import torch.backends.cudnn as cudnn
from torchvision.transforms import Compose, Normalize, ToTensor
import torchvision.utils as vutils
from net import NetS

# Debug MWB
import sys
print('__Python VERSION:', sys.version)
print('__pyTorch VERSION:', torch.__version__)
print('__CUDNN VERSION:', torch.backends.cudnn.version())
print('__Number CUDA Devices:', torch.cuda.device_count())
print('Active CUDA Device: GPU', torch.cuda.current_device())
print ('Available devices ', torch.cuda.device_count())
# End Debug MWB

parser = argparse.ArgumentParser(description='Arguments for predict routine')
parser.add_argument('--statedict', required=True, help='filename of trained network state')
parser.add_argument('--inputfile', required=True, help='filename of image to run through network')
parser.add_argument('--ngpu', type=int, default=1, help='number of GPUs to use, for now it only supports one GPU')
parser.add_argument('--outdir', default='./outdir', help='stores predicted images')
parser.add_argument('--cuda', default=True, help='using GPU or not')
opts = parser.parse_args()

print(opts)

try:
    os.makedirs(opts.outdir)
except OSError:
    pass

cuda = opts.cuda

cudnn.benchmark = True

netS = NetS(ngpu=1)
netS.cuda()
netS.eval()

netS.load_state_dict(torch.load(opts.statedict))

image = Image.open(opts.inputfile).convert('RGB')
image = image.resize((128, 128), Image.BILINEAR)

img_transform = Compose([
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406],std=[0.229, 0.224, 0.225])
])

print("type(image) = ", type(image))
data = img_transform(image)
print("type(data) = ", type(data))
print("data.size() = ", data.size())
data = data.unsqueeze(0)
print("data.size() = ", data.size())
input = torch.autograd.Variable(data)
print("type(input.data) = ", type(input.data))
#if cuda:
input = input.cuda()

print("type(input.data) = ", type(input.data))

pred = netS(input)
print("type(pred) = ", type(pred))
print("pred.size() = ", pred.size())
vutils.save_image(pred.data, '%s/result_val.png' % opts.outdir, normalize=True)


