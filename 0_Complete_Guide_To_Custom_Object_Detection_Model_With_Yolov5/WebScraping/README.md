# Web Scraping
This guide explains how to scrape image from Google using this script.

---
## Environment Setup

Follow the setup guide [here](../README.md#getting-started).

---

## User Guide

1. Activate the conda environment.\

    ```
    conda activate object-detection
    ```

2. Scrape images with script\
*note: replace variables with <<>> to respective arguments*

    ```
    python ./src/main.py <<keyword to scrape>> <<folder name>>
    ```
    Eg.
    ```
    python ./src/main.py wheelchair wheelchair1
    ```


---

## Output

### Image folder
the result will be stored in `./images/<<folder name>>` folder with the name of `<<folder name>>_<<numbers>>.png` \
Eg.\
 `./images/wheelchair1/wheelchair1_0001.png`