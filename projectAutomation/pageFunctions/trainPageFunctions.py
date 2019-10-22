from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

class trainfunctions:
    
    def setFromLocation(self,driver):
        driver.find_element_by_xpath("//input[@id='from_station']").send_keys("Secunderabad Junction (SC)")
    
    def setToLocation(self,driver):
        driver.find_element_by_xpath("//input[@id='to_station']").send_keys("Guntur Junction (GNT)")
        
    def selectClass(self,driver):
        Select(driver.find_element_by_xpath("//select[@id='trainClass']")).select_by_index(4)
        
    def selectDate(self,driver):
        driver.find_element_by_xpath("//table[1]//tbody[1]//tr[4]//td[4]//a[1]").click()
        
    def selectAdults(self,driver):
        Select(driver.find_element_by_xpath("//select[@id='train_adults']")).select_by_index(2)
        
    def clickSearch(self,driver):
        driver.find_element_by_xpath("//button[@id='trainFormButton']").click()
        time.sleep(5)