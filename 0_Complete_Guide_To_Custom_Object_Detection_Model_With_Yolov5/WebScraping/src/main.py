from page import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import util.image_downloader as downloader
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("keyword", type=str, help="Keyword to search for google image scraping")
parser.add_argument("folder_name", type=str, help="The folder name to store the scrapped images in")
parser.add_argument("img_num", type=int, default=-1, help="The number of images to scrape")

args = parser.parse_args()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/")

main_page = GoogleMainPage(driver)

search_page = main_page.search_title(args.keyword)

image_search_page = search_page.to_image_search()

print("start scraping image...")

image_search_page.scroll_till_end()

print("collecting image source...")

img_src_list = image_search_page.get_img_source_list()

print("start downloading image...")

driver.close()

downloader.save_images(img_src_list, args.folder_name, args.img_num)

print("finish downloading images...")