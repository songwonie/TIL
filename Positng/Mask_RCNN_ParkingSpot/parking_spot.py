"""
Mask R-CNN을 이용하여 주차 공간 찾기!

아래의 'mrcnn' 받는 gitHub 주소 : https://github.com/matterport/Mask_RCNN
 
    $ git clone https://github.com/matterport/Mask_RCNN.git
"""
import os
import numpy as pd 
import cv2
import mrcnn.config
import mrcnn.utils
from mrcnn.model import MaskRCNN 
from pathlib import Path  # dir 저장 path 관련?


# configuration that will be used by the Mask-RCNN library
class MaskRCNN_Config(mrcnn.config.Config):
    NAME = "coco_pre_trained_model_config"
    IMAGES_PER_GPU = 1
    GPU_COUNT = 1
    NUM_CLASSES = 80 + 1 # COCO dataset has 80 classes + one background class
    DETECTION_MIN_CONFIDENCE = 0.6


# Mask R-CNN으로 detection한 결과들 중에서 cars와 trucks 만을 Filtering 해서 가져옴
def get_car_boxes(boxes, class_ids):
    car_boxes = []

    for i, box in enumerate(boxes):
        # class가 trucks/cars가 아닌 경우 skip!
        if class_ids[i] in [3, 8, 6]:
            car_boxes.append(box) # car, truck인 경우 append! 

    return np.array(car_boxes)  # car, truck인 경우를 담은 list return!


# proj dir
ROOT_DIR = Path('.')

# Directory to save logs and trained-model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# local PATH, trained model
COCO_MODEL_PATH = os.path.join(ROOT_DIR, "mask_rcnn_coco.h5")

# Create a Mask-RCNN model in inference mode
model = MaskRCNN(mode='inference', model_dir= , config=MaskRCNN_Config())

# load pre-trained model 
model.load_weights(COCO_MODEL_PATH, by_name=True)

# Video-PATH
VIDEO_SOURCE = 'test_images/parking.mp4'

# Location of parking spaces
parked_car_boxes = None


# 동영상 받아오기
video_capture = cv2.VideoCapture(VIDEO_SOURCE)

# Loop each frame of video
while video_capture.isOpened():
    success, frame = video_capture.read()
    if not success:
        break

    # Open-cv, Convert image, BGR to RGB COLOR
    # rgb_img = frame[ :, :, ::-1]
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) # 이건 안되나?

    # Mask-RCNN 통해, image detection get results
    results = model.detect([rgb_img], verbose=0)
