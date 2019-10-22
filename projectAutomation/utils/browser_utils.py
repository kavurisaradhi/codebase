from selenium import webdriver

class Browser:
    
    def openBrowser(self):
        driver=webdriver.Chrome(executable_path="C:/Users/katta/Downloads/Drivers/chromedriver.exe")
        return driver
    def openUrl(self,driver):
        driver.get("https://www.cleartrip.com/")
    def closeBrowser(self,driver):
        driver.quit()