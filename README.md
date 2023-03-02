# TextBoxes: A Fast Text Detector with a Single Deep Neural Network

This is the work of https://github.com/MhLiao/TextBoxes_plusplus with brief modification + implementaion for OpenCV > 4.
This project is done in Google Colaboratory.

Recommend: [TextBoxes++](https://github.com/MhLiao/TextBoxes_plusplus) is an extended work of TextBoxes, which supports oriented scene text detection. The recognition part is also included in [TextBoxes++](https://github.com/MhLiao/TextBoxes_plusplus).

### Introduction
This paper presents an end-to-end trainable fast scene text detector, named TextBoxes, which detects scene text with both high accuracy and efficiency in a single network forward pass, involving no post-process except for a standard nonmaximum suppression. For more details, please refer to our [paper](https://arxiv.org/abs/1611.06779).

### Citing TextBoxes
Please cite TextBoxes in your publications if it helps your research:

    @inproceedings{LiaoSBWL17,
      author    = {Minghui Liao and
                   Baoguang Shi and
                   Xiang Bai and
                   Xinggang Wang and
                   Wenyu Liu},
      title     = {TextBoxes: {A} Fast Text Detector with a Single Deep Neural Network},
      booktitle = {AAAI},
      year      = {2017}
    }

### Using this repository
1. Run TextBox.ipynb (All the process explained below is implemeted here.)

### Contents
1. [Installation](#installation)
2. [Download](#download)
3. [Test](#test)
4. [Train](#train)
5. [Performance](#performance)

### Installation
1. Get the code. We will call the directory that you cloned Caffe into `$CAFFE_ROOT`
  ```Shell
  git clone https://github.com/treeleafrnd/TextBox.git
  
  cd TextBoxes
  
  make -j8
  
  make py
  ```

### Test
1. run "python examples/demo.py".
2. You can modify the "use_multi_scale" in the "examples/demo.py" script to control whether to use multi-scale or not.
3. The results are saved in the "examples/results/".

### Preparing Dataset
1. Training is done in  custom dataset. The files are included in /dataset/
2. Before creating lmdb train.txt/test.txt are created. (included in /data/text/)
3. sh create.sh is executed to create lmdb dataset (included in /data/lmdb)

### Train
1. run "python examples/TextBoxes/train_icdar13.py".
2. set the model parameters accordingly.


### Performance
1. Using the dataset, setting the iteration to 200 it achieves 69% accuracy.

Before Training

![demo_before](https://user-images.githubusercontent.com/99968233/222384689-d166e8cd-3273-4fe0-aae9-5df715dfe49d.jpeg)

After Training

![demo_after](https://user-images.githubusercontent.com/99968233/222384676-3980dfaf-3a41-45c7-a079-214b099257a4.png)

### Text Annotation for training (Labeling done using LabelImg)
The reference xml file is as following:
  
        <?xml version="1.0" encoding="utf-8"?>
        <annotation>
            <object>
                <name>text</name>
                <bndbox>
                    <xmin>158</xmin>
                    <ymin>128</ymin>
                    <xmax>411</xmax>
                    <ymax>181</ymax>
                </bndbox>
            </object>
            <object>
                <name>text</name>
                <bndbox>
                    <xmin>443</xmin>
                    <ymin>128</ymin>
                    <xmax>501</xmax>
                    <ymax>169</ymax>
                </bndbox>
            </object>
            <folder></folder>
            <filename>100.jpg</filename>
            <size>
                <width>640</width>
                <height>480</height>
                <depth>3</depth>
            </size>
        </annotation>

### Changes made in the repository:

1. Makefile.config
2. Makefile
3. src/caffe/util/io.cpp
4. src/caffe/util/bbox_util.cpp
5. src/caffe/util/im_transforms.cpp
6. src/caffe/layers/window_data_layer.cpp
7. src/caffe/layers/video_data_layer.cpp


 INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial/ /usr/include/hdf5/serial/ /usr/include/hdf5/serial/ (Makefile.config)
 LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib  /usr/lib/x86_64-linux-gnu/hdf5/serial (Makefile.config)

 LIBRARIES += opencv_core opencv_highgui opencv_imgproc opencv_videoio (Makefile)

 Annotate CPU_ONLY := 1 in Makefile.config (GPU requirement is mandatory)

 PYTHON_LIBRARIES := boost_python38 python3.8
 PYTHON_INCLUDE := /usr/include/python3.8 \
                 /usr/lib/python3.8/dist-packages/numpy/core/include


After compiling make.py using GPU sucessfully
edit:
    caffe/io.py ----> line 296 -----> as_grey to as_gray
    demo_det.py ----> xrange to range
    
All these and other changes in .cpp and .py files which are necessary for OpenCV version > 4 users are done in this repository.
Similarly, change for google colab users has been done as needed.

Training and Testing dataset are collected from GoodNotes.
Fine tuning is done in ICDAR dataset with addition 12 images from goodnotes. 



