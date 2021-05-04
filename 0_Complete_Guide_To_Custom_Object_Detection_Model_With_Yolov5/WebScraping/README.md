# Web Scraping
This guide explains how to scrape image from Google using this script.

---
## Environment Setup

Follow the setup guide [here](../README.md#getting-started).

---

## User Guide
1. Open terminal from this folder.

2. Activate the conda environment.

    ```
    conda activate object-detection
    ```

3. Scrape images with script\
*Note: Replace variables with <<>> to respective arguments*

    * **keyword to scrape**: The keyword to be searched in Google.

    * **folder name**: The folder name to store the scraped image. It will also be used as the prefix of the name of scraped images. **Names with space are not recommended to be used here**.

    * **number of images**: Specify the number of images to be scraped. Enter "-1" to scrape all images.

    ```
    python ./src/main.py <<keyword to scrape>> <<folder name>> <<number of images>>
    ```
    Eg.
    ```
    python ./src/main.py "wheelchair" "wheelchair1" -1  
    ```


---

## Output

### Image folder
the result will be stored in `./images/<<folder name>>` folder with the name of `<<folder name>>_<<numbers>>.png` \
Eg.\
 `./images/wheelchair1/wheelchair1_0001.png`