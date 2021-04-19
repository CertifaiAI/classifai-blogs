# Web Scraping
This guide explains how to scrape image from Google using this script.

---

## Getting Started
### Install Anaconda

Download and install [Anaconda](https://www.anaconda.com/products/individual).

### Install ChromeDriver

Download [ChromeDriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver#quick-installation)

### Environment Setup

Setup the conda environment by

    
    conda env create -f environment.yml
    

---

## User Guide

1. Activate the conda environment by

    ```
    conda activate selenium-web-scraping
    ```

2. Run python script by

    ```
    python ./src/main.py <keyword to scrape> <folder name>
    ```

---

## Sample Output

### Image folder
the result will be stored in *./images/\<folder name>* folder with the name of *\<folder name>_\<numbers>.png* \
Eg. ./images/wheelchair1/wheelchair1_0001.png