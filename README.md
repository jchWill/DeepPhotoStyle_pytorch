# Updated to fit torch 1.x.x

This repo is forked from [ray075hl/DeepPhotoStyle_pytorch](https://github.com/ray075hl/DeepPhotoStyle_pytorch).

Some of the codes in the original repo are outdated,  so I have done a little modification to let the code fit torch > 1.10.0.

The current code is tested under pyTorch 1.10.1 with CUDA 11.x, Python > 3.8.

## Usage

```bash
git clone 

https://github.com/jchWill/DeepPhotoStyle_pytorch.git

cd DeepPhotoStyle_pytorch

bash download_seg_model.sh 




python main.py --style_image path_style_image --content_image path_content_image --clear_dir {true/True/other}do_clear_temp_results


```

Or you may import the packed "pipeline" method in main.py into your project.

If you have any problems, you may make an issue.

The following are from the original README.





# DeepPhotoStyle_pytorch[(中文说明)](README_ZH.md)

Recreating paper ["Deep Photo Style Transfer"](https://arxiv.org/abs/1703.07511) with pytorch.
This project supply semantic segmentation code.
## Here are some experiment results
![](./doc_image/ex_001.jpg)
![](./doc_image/ex_002.png)
![](./doc_image/ex_003.jpg)
## Setup
Install [pytorch](https://pytorch.org/) version 0.4.1 with CUDA
Python version: python3.6

```
git clone 

https://github.com/ray075hl/DeepPhotoStyle_pytorch.git

cd DeepPhotoStyle_pytorch

sh download_seg_model.sh 




python main.py --style_image path_style_image --content_image path_content_image
```
**download_seg_model site may not available. You can download segmentation model** [here](https://drive.google.com/open?id=1kkeWEQyyLPELBDbxNljEWBn4DBEwP1ZZ)  

## Notice
The semantic segmentation result of image pair(style and content) have a huge impact to the quality of transfered image. Check the segmentation result to see whether the relative semantic of image pair as you expected(for example, sky match sky, person match person etc.) or not.

## Reference
[1] All the code of semantic segmentation from here [Semantic-segmentation-pytorch](https://github.com/CSAILVision/semantic-segmentation-pytorch). I appreciate this fantastic project greatly.

[2] Base framework of neural style transfer.  [Neural Transfer with PyTorch](https://pytorch.org/tutorials/advanced/neural_style_tutorial.html)

[3] Compute laplacian matirx. [Closed-form-matting
](https://github.com/MarcoForte/closed-form-matting)

[4] ["Deep Photo Style Transfer"](https://arxiv.org/abs/1703.07511)

[5] Post-processing of photo to photo.[Visual Attribute Transfer through Deep Image Analogy](https://arxiv.org/abs/1705.01088)
