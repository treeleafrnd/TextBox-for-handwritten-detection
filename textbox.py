# -*- coding: utf-8 -*-
"""Textbox.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AHsj30Okqpm2zq5GmgI8HsGNgSlKGRMm
"""

from google.colab import drive
drive.mount('/content/drive')

"""**CHECKING GRAPHICS**"""

!nvidia-smi

"""**CREATING ENVIRONMENT**"""

# Commented out IPython magic to ensure Python compatibility.
# %pwd

cd drive/MyDrive/TextBoxes

#cp Makefile.config.example Makefile.config

!apt-get install caffe-cpu

pip install make

pip install cmake

!pip install protobuf==3.7.1

pip install numpy

import caffe

caffe.__version__

!sudo apt-get install libprotobuf-dev protobuf-compiler

!sudo apt-get install libopencv-dev python3-opencv

!sudo apt-get install libopenblas-dev

!sudo apt-get install libboost-all-dev

!sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler

!sudo apt-get install the python-dev

!sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev

import cv2
cv2.__version__

!apt-get install python-numpy

!sudo ln -s /usr/include/opencv4/opencv2 /usr/include/opencv2

pip install opencv-contrib-python

"""**COMPILING TEXTBOX**"""

#!rm -rf ./build*/

#!make clean

#!make -j8

#!make py

"""**RUNNING DEMO**"""

#! python examples/TextBoxes/demo.py

"""**PREPARING TRAINING DATASET**"""

#! chmod 777 /content/drive/MyDrive/TextBoxes/build/tools/convert_annoset

#! bash ./data/text/create_data.sh

"""**TRAINING CUSTOM DATASET**"""

# Commented out IPython magic to ensure Python compatibility.
# %pwd

! chmod 777 ./build/tools/caffe

! python examples/TextBoxes/train_icdar13.py

"""**RUNNING DEMO AFTER TRAINING**"""

! python examples/TextBoxes/demo.py

