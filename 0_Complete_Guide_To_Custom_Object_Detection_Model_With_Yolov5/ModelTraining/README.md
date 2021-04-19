# Model Training

This guide explains how to train your own **custom dataset** with YOLOv5. *This script is levaraging the [repo](https://github.com/ultralytics/yolov5)*

The jupyter notebook script is built to train in **Google Colab**. Certain changes to be done to the script are expected if training is performed locally.

---

## User Guide

### Data Preparation
#### Dataset Structure
The structure of dataset should be same as the sample in this repository :
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
    
    *image* \
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


### Model training
1. Zip the dataset folder into *dataset.zip*

2. Upload jupyter notebook script to google drive

3. Double click to open Google Colab session

4. Go to files, upload the *dataset.zip*

5. Run the scripts

6. After running all the scripts, the weights are save in your drive. Download it for evaluation and testing

---

## Model Inference

### Install Anaconda

Download and install [Anaconda](https://www.anaconda.com/products/individual).

### Environment Setup

Setup the conda environment by

    conda env create -f environment.yml

Activate the conda environment by

    conda activate selenium-web-scraping

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
To run inference script \ 
*note : change variables with << >>*

```
python ./src/detect.py --source <<source>> --weights <<weights name>> --conf <<threshold>>
```

---
## Sample Output
