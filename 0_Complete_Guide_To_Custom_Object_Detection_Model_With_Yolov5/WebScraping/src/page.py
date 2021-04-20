from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from locators import *
from urllib.parse import unquote
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(driver, 100)
    
    def find_element(self, locator):
        return self.wait.until(lambda driver: driver.find_element(*locator))

    def find_elements(self, locator):
        return self.wait.until(lambda driver: driver.find_elements(*locator))

    def execute_script(self, script):
        return self.driver.execute_script(script)

    def click(self, locator):
        self.find_element(locator).click()
    
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)


class GoogleMainPage(BasePage):
    """Google main page action methods come here"""

    def search_title(self, text):
        """Enter text into google search box and press enter"""

        element = self.find_element(GoogleMainPageLocators.INPUT)
        element.send_keys(text + Keys.RETURN)
        return GoogleSearchResultsPage(self.driver)


class GoogleSearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def to_image_search(self):
        """Go to google search image page"""

        self.click(GoogleSearchResultPageLocators.IMAGE_BUTTON)
        return GoogleImageResultsPage(self.driver)

class GoogleImageResultsPage(BasePage):
    """Image search results page action methods come here"""

    def load_status(self):
        """check if all images loaded"""
        """ -1 => not-loaded, 0 => need to click to load, 1 => fully-loaded"""
        
        element = self.find_element(GoogleImageResultPageLocators.RESULT_INDICATOR)
        status = element.get_attribute("data-status")

        if status == "3":
            return 1
        elif status == "5":
            return 0
        else:
            return -1
    
    def scroll_till_end(self):
        """scroll to load images"""

        while True:
            cur_height = self.execute_script("return window.pageYOffset + document.documentElement.clientHeight")
            total_height = self.execute_script("return document.body.scrollHeight")

            self.execute_script(f"window.scrollTo(0,{total_height})")

            if (self.load_status() == 0 and cur_height == total_height):
                self.click(GoogleImageResultPageLocators.RESULT_INDICATOR)
            
            if self.load_status() == 1:
                break

        return 

    def get_img_source_list(self):
        """click images to get high resolution images"""

        output_list = list()

        img_list = self.find_elements(GoogleImageResultPageLocators.RESULT_IMAGES)

        for img in img_list:

            try:
                img.click()
            except:
                continue            

            #if can't get the image source, skip it
            try:
                image_url = img.get_attribute("href")

                start_idx = image_url.index("imgurl=") + 7
                end_idx = image_url.index('&', start_idx)
                image_src = image_url[start_idx: end_idx]
                output_list.append(unquote(image_src))

            except:
                continue

            
        return output_list
