from selenium import webdriver
from utils.browser_utils import *
class home:
    
    def verifyHomePage(self,driver):
        element=driver.find_element_by_xpath("//h1[contains(text(),'Search flights')]").text
        if element=="Search flights":
            print('i am into homepage')
        
        