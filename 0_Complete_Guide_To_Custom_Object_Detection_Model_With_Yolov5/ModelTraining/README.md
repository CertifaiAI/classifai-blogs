# Model Training

This guide explains how to train your own **custom dataset** with YOLOv5. *This script is levaraging the [repo](https://github.com/ultralytics/yolov5)*

The jupyter notebook script is built to train in **Google Colab**. Certain changes to be done to the script are expected if training is performed locally.

---

## User Guide

### Data Preparation
#### Dataset Structure
The structure of dataset should be same as provided [dataset.zip](link-to-dataset) :
```
.
+-- dataset
    +-- train
    |   +-- images
    |   |   +-- <<images>>
    |   +-- labels
    |       +-- <<labels>>  
    +-- val
    |   +-- images
    |   |   +-- <<images>>
    |   +-- labels
    |       +-- <<labels>> 
    +-- test
    |   +-- images
    |   |   +-- <<images>>
    |   +-- labels
    |       +-- <<labels>> 
    +-- data.yaml

```
1. train/valid/test folder
    
    train/valid/test folder should contain two folders: *images* & *labels* \
    *images* folder contains all the images \
    *labels* folder contains all the label file in *txt format*:
    ```
    label x y w h
    ```

2. data.yaml 

    *data.yaml* is a config file for the model on data path and class names \
    *note : replace the \<number of classes> and \<array of class name>*


    ```
    train: ../train/images
    val: ../valid/images

    nc: <number of classes>
    names: [<array of class names>]
    ```

*In the project, data augmentation and train-validation-test split is done using [roboflow](https://roboflow.com/). But it is optional to use it, as long as the dataset is following the structure mentioned above.*

### Model training
1. Zip the dataset folder into *dataset.zip*\
    *image*

2. Upload jupyter notebook script to google drive\
    *image*

3. Double click to open Google Colab session\
    *image*

4. Go to files, upload the *dataset.zip*\
    *image*

5. Run the scripts and follow the instructions written in the jupyter notebook\
    *image*

6. After running all the scripts, the weights are save in your drive. Download it for inference.\
    *image*

---

## Model Inference

### Environment Setup

Activate the conda environment by

    conda activate object-detection

### Inference

#### Weights
For conventions, save the weights of the model into *./src/weights* folder

#### Source of Data
Multiple sources of data are able to be run for inference: \

```
python ./src/detect.py --source 0  # webcam
                                file.jpg  # image 
                                file.mp4  # video
                                path/  # directory
                                path/*.jpg  # glob
                                'https://youtu.be/NUsoVlDFqZg'  # YouTube video
                                'rtsp://example.com/media.mp4'  # RTSP, RTMP, HTTP stream
```

#### Run Inference 
Run the inference script\
*note : replace the variables with << >> to the respective arguments*

```
python ./src/detect.py --source <<source>> --weights <<weights name>> --conf <<threshold>>
```

---
## Sample Output
