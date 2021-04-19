# Complete Guide to Custom Object Detection Model with YOLOv5

[image of wheel chair detection]

In this repository, a complete guide to build a custom object detection model using YOLOv5 will be conducted.

Go to medium post for more details explanation.

## Scripts
- WebScraping
    
    Script to scrape data from Google using Selenium

- ModelTraining

    GoogleColab Script to train YOLOv5 model

## Step-by-step Guide
1. Web Scraping

    Scrape data from Google using Selenium. Refer [README.md](./WebScraping/README.md) for details guidelines.

2. Data Filtering

    Remove irrelavant data from scraped data.

3. Data Annotation

    Label scraped data using [Classifai](https://github.com/CertifaiAI/classifai)

4. Data Augmentation & Train-Validation-Test Split

    Data Augmentation : Increase sample size of data & regulatization method\
    Train-Validation-Test Split : Split dataset into train/validation/test set\

    This is done using [roboflow](https://roboflow.com/)

5. Model Training

    Train YOLOv5 model using GoogleColab. Refer [README.md](./ModelTraining/README.md) for details guidelines.
