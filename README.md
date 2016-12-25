# TextBoxes: A Fast Text Detector with a Single Deep Neural Network

### Introduction
This paper presents an end-to-end trainable fast scene text detector, named TextBoxes, which detects scene text with both high accuracy and efficiency in a single network forward pass, involving no post-process except for a standard nonmaximum suppression. For more details, please refer to our [arXiv paper](https://arxiv.org/abs/1611.06779).

### Citing TextBoxes
Please cite TextBoxes in your publications if it helps your research:

    @article{DBLP:journals/corr/LiaoSBWL16,
      author    = {Minghui Liao and
                   Baoguang Shi and
                   Xiang Bai and
                   Xinggang Wang and
                   Wenyu Liu},
      title     = {TextBoxes: {A} Fast Text Detector with a Single Deep Neural Network},
      journal   = {CoRR},
      volume    = {abs/1611.06779},
      year      = {2016},
    }

### Contents
1. [Installation](#installation)
2. [Models](#models)

### Installation
1. Get the code. We will call the directory that you cloned Caffe into `$CAFFE_ROOT`
  ```Shell
  git clone https://github.com/MhLiao/caffe.git
  
  cd caffe
  
  git checkout TextBoxes
  
  make -j8
  
  make py
  ```

### Models
1. Models trained on ICDAR 2013: https://www.dropbox.com/s/lq11l6so2t0fsoq/TextBoxes_icdar13.caffemodel?dl=0
