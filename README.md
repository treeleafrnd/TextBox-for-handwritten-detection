# TextBoxes: A Fast Text Detector with a Single Deep Neural Network

### Declaration
The test model of ICDAR 2013 dateset and the single scale test codes were released here. We will released the multi-scale test codes and the training codes later.

### Introduction
This paper presents an end-to-end trainable fast scene text detector, named TextBoxes, which detects scene text with both high accuracy and efficiency in a single network forward pass, involving no post-process except for a standard nonmaximum suppression. For more details, please refer to our [arXiv paper](https://arxiv.org/abs/1611.06779).

### Citing TextBoxes
Please cite TextBoxes in your publications if it helps your research:

    @article{LiaoSBWL16TextBoxes,
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
3. [Test](#test)
4. [Performance](#performance)

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
1. Models trained on ICDAR 2013: https://www.dropbox.com/s/g8pjzv2de9gty8g/TextBoxes_icdar13.caffemodel?dl=0

### Test
1. Download the ICDAR 2013 DataSet
2. Download the Models trained on ICDAR 2013
3. Modify the related paths in the "examples/TextBoxes/test_icdar13.py"
4. run "python examples/test_icdar13.py"

### Performance
1. Using the given test code, you can achieve an F-measure of about 80% on ICDAR 2013 with a single scale.
2. You can change the given code for multi-scale inputs and do a non-maximum suppression with the multi-scale results. You will achieve an F-measure of about 86% on ICDAR 2013 in this way.
    We will update the multi-scale test codes later.
3. More performance information, please refer to the paper and Task1 and Task4 of Challenge2 on the ICDAR 2015 website: http://rrc.cvc.uab.es/?ch=2&com=evaluation

Please let me know if you encounter any issues.
