import re
import sys
import os
import glob
import numpy as np
import matplotlib.pyplot as plt

def plot_stats (filename, fig_num):
    max_re = re.compile("^Max mIoU:(?P<Mmiou>\s\d+\.\d+)")
    miou_re = re.compile("mIoU:(?P<miou>\s\d+\.\d+)")
    dice_re = re.compile("Dice:(?P<dice>\s\d+\.\d+)")
    bDice_re = re.compile("===> Epoch\[(\d+)\]\(\d+\/\d+\): Batch Dice: (-?\d\.\d+)")
    gloss_re = re.compile("===> Epoch\[(\d+)\]\(\d+\/\d+\): G_Loss: (-?\d\.\d+)")
    dloss_re = re.compile("===> Epoch\[(\d+)\]\(\d+\/\d+\): D_Loss: (-?\d\.\d+)")
    cur_epoch = -1
    max_IoU = []
    mIoU = {}
    dice = {}
    bDice = {}
    gLoss = {}
    dLoss = {}
    with open(filename, 'r') as f:
        for line in f:
            m = max_re.match(line)
            if m:
                max_IoU.append(float(m.group(1)))
            m = bDice_re.match(line)
            if m:
                cur_epoch = int(m.group(1))
                bDice[cur_epoch] = float(m.group(2))
            m = gloss_re.match(line)
            if m:
                cur_epoch = int(m.group(1))
                gLoss[cur_epoch] = float(m.group(2))
            m = dloss_re.match(line)
            if m:
                cur_epoch = int(m.group(1))
                dLoss[cur_epoch] = float(m.group(2))
            m = miou_re.match(line)
            if m:
                mIoU[cur_epoch] = float(m.group(1))
            m = dice_re.match(line)
            if m:
                dice[cur_epoch] = float(m.group(1))
    plt.style.use('seaborn-bright')
    plt.figure(fig_num)
    fig_num += 1
    plt.title(filename)
    plt.plot(mIoU.keys(), mIoU.values(), label='mIoU')
    plt.plot(dice.keys(), dice.values(), label='Dice')
    max_dice = max(dice.values())
    mdice_array = np.ones(len(dice.keys())) * max_dice
    plt.plot(dice.keys(), mdice_array, label=max_dice)
    print("Max dice = {}".format(max_dice))
    max_IoU = max(mIoU.values())
    print("Max mIoU = {}".format(max_IoU))
    mIoU_array = np.ones(len(mIoU.keys())) * max_IoU
    plt.plot(mIoU.keys(), mIoU_array, label=max_IoU)
    plt.xlabel("Epoch")
    plt.legend()
    plt.figure(fig_num)
    fig_num += 1
    plt.title(filename)
    max_bDice = max(bDice.values())
    print("Max bDice = {}".format(max_bDice))
    plt.plot(bDice.keys(), bDice.values(), label='Batch Dice')
    bDice_array = np.ones(len(bDice.keys())) * max_bDice
    plt.plot(bDice.keys(), bDice_array, label=max_bDice, color='red')
    plt.legend()
    plt.xlabel("Epoch")
    plt.ylabel("Batch Dice")
    plt.figure(fig_num)
    fig_num += 1
    plt.title(filename)
    plt.plot(gLoss.keys(), gLoss.values(), label='G_Loss')
    plt.plot(dLoss.keys(), dLoss.values(), label='D_Loss')
    plt.plot(dLoss.keys(), [dLoss[key] + gLoss[key] for key in dLoss.keys()], label='diff')
#    print("Max gLoss = ", max(gLoss.values()))
#    print("Min dLoss = ", max(dLoss.values()))
    plt.xlabel("Epoch")
    plt.legend()
    #plt.show()


print("sys.argv = {}".format(sys.argv))
fig_num = 1
if (len(sys.argv) > 1):
    print(sys.argv[1:])
    for arg in sys.argv[1:]:
        print('file = {}'.format(arg))
        plot_stats (arg, fig_num)
        fig_num += 3
else:
    for file in glob.glob('./*.out'):
        print('file = {}'.format(file))
        plot_stats (file, fig_num)
        fig_num += 3
plt.show()
