from pageFunctions.trainPageFunctions import trainfunctions
import time

class trains:
    
    def NavigateToTrains(self,driver):
        driver.find_element_by_xpath("//a[contains(text(),'Trains')]").click()
        time.sleep(5)
    def searchTrains(self,driver):
        trainfunctions().setFromLocation(driver)
        trainfunctions().setToLocation(driver)
        trainfunctions().selectClass(driver)
        trainfunctions().selectDate(driver)
        trainfunctions().selectAdults(driver)
        trainfunctions().clickSearch(driver)
    def verifySearch(self,driver):
        driver.switch_to.frame('modal_window')
        name=driver.find_element_by_xpath("//*[@id='ContentFrame']/div/div/h1").text
        if name =="Sign in to Cleartrip":
            print("search done successfully") 