from utils.browser_utils import * 
from pages.homePage import home
from components.trains import trains

def test1():
    driver=Browser().openBrowser()
    Browser().openUrl(driver)
    home().verifyHomePage(driver)
    trains().NavigateToTrains(driver)
    trains().searchTrains(driver)
    trains().verifySearch(driver)
    Browser().closeBrowser(driver)