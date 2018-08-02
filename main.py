import sys

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image


import torchvision.transforms as transforms
import torchvision.models as models

import matplotlib.pyplot as plt

import config
import utils

sys.path.append('seg')
from seg.segmentation import *
from model import *
from merge_index import *

if __name__ == '__main__':

    #--------------------------
    seg_result = segmentation('1.jpg').squeeze(0)
    channel, height_, width_ = seg_result.size()
    merged_seg = np.zeros((117, height_, width_), dtype='int')
    for classes in merge_classes:
        for index, each_class in enumerate(classes):
            if index == 0:
                zeros_index = each_class
                base_map = seg_result[each_class, :, :].clone()
            else:
                base_map = base_map | seg_result[each_class, :, :]
        seg_result[zeros_index, :, :] = base_map

    count = 0
    for i in range(150):
        if i not in del_classed:
            merged_seg[count, :, :] = seg_result[i, :, :]
            count += 1
            print(count)
        else:
            pass

    print(merged_seg.shape)
    exit()
    #--------------------------

    device = torch.device(config.device0)

    imsize = 512 if torch.cuda.is_available() else 128  # use small size if no gpu

    style_img = utils.load_image('style.jpg', imsize)
    content_img = utils.load_image('content.jpg', imsize)

    style_img = utils.image_to_tensor(style_img).unsqueeze(0)
    content_img = utils.image_to_tensor(content_img).unsqueeze(0)

    style_img = style_img.to(device, torch.float)
    content_img = content_img.to(device, torch.float)

    utils.show_pic(style_img, 'style image')
    utils.show_pic(content_img, 'content image')

    # -------------------------
    cnn = models.vgg19(pretrained=True).features.to(config.device0).eval()

    cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(config.device0)
    cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(config.device0)

    input_img = torch.randn(1, 3, imsize, imsize).to(config.device0)

    output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                content_img, style_img, input_img)

    utils.show_pic(output, title='final result')
    plt.ioff()
    plt.show()


