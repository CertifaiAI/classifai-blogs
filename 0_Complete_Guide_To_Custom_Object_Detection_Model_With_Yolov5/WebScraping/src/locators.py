from selenium.webdriver.common.by import By

class GoogleMainPageLocators(object):
    """A class for main page locators. All google main page locators should come here"""

    INPUT = (By.CSS_SELECTOR, "INPUT[type='text']")

class GoogleSearchResultPageLocators(object):
    """A class for search results locators. All google search results locators should come here"""

    IMAGE_BUTTON = (By.XPATH, "//div[@class='MUFPAc']//child::a[contains(text(),'Images')]")

class GoogleImageResultPageLocators(object):
    """A class for search results locators. All google image search results locators should come here"""
    
    RESULT_INDICATOR = (By.XPATH, "//div[@class='DwpMZe ']")
    RESULT_IMAGES = (By.XPATH, "//a[@class='wXeWr islib nfEiy mM5pbd']")