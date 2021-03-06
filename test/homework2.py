from selenium                                       import webdriver

from selenium.webdriver.support.ui                  import WebDriverWait

from selenium.webdriver.common.by                   import By

from selenium.webdriver.common.action_chains        import ActionChains

from selenium.webdriver.common.keys                 import Keys

import unittest

import time


class sendKeys(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")
        driver.maximize_window()
    
    
    
    def test_sendKeys(self):
        #Locators
        #searchFieldName      = "q"
        quantityNameLocator = "Quantity"
        
        quantityElement   = WebDriverWait(driver, 10).\
                               until(lambda driver: driver.find_element_by_name(quantityNameLocator))
        
        actions = ActionChains(driver)
        actions.send_keys_to_element(quantityElement, Keys.ENTER)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.perform()
        time.sleep(5)

        #WebDriverWait(driver, 10).\
            #until(lambda driver: driver.find_element_by_xpath(turtlePictureLocator))



    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()



