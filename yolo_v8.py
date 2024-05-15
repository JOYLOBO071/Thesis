# -*- coding: utf-8 -*-
"""yolo v8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WXLG0nGFXuLe1-i-j-5yV-ysPyzeN2L3
"""

!nvidia-smi

"""INSTALL YOLO V8"""

# Pip install method (recommended)

!pip install ultralytics==8.0.20

from IPython import display
display.clear_output()

import ultralytics
ultralytics.checks()

from ultralytics import YOLO

from IPython.display import display, Image

"""Custom Training

CONNECT WITH DRIVE
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/yolov8

!ls

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/MyDrive/yolov8

!yolo task=detect mode=train model=yolov8s.pt data= data.yaml epochs=5 imgsz=640 plots=True

!ls runs/detect/train/

Image(filename='runs/detect/train2/confusion_matrix.png', width=600)

Image(filename='runs/detect/train2/results.png', width=600)

Image(filename='runs/detect/train2/val_batch0_pred.jpg', width=600)

!yolo task=detect mode=val model=runs/detect/train2/weights/best.pt data=data.yaml

!yolo task=detect mode=predict model=runs/detect/train2/weights/best.pt conf=0.25 source=data/test/images